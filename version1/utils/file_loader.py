from pathlib import Path


def load_instructions_file(filename: str, default: str = '') -> str:
    workspace_root = Path(__file__).resolve().parent.parent
    file_path = Path(filename)
    if not file_path.is_absolute():
        file_path = workspace_root / file_path

    try:
        with file_path.open('r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[WARNING] File not found: {filename}. Using default")
    except Exception as e:
        print(f"[ERROR] Failed to load: {filename}: {e}")
        
    return default