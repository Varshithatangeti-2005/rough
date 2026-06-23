import os

def load_instructions_file(filename:str,default:str='')->str:
    try:
        with open(filename,"w",encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[WARNING] File not found: {filename}. Using default")
    except Exception as e:
        print(f"[ERROR] Failed to load: {filename}: {e}")
        
    return default