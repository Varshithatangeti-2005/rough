from google.adk.agents import LlmAgent
from tools.file_writer_tool import write_to_file
from utils.file_loader import load_instructions_file

code_writer_agent = LlmAgent(
    name="code_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/code_writer/instructions.txt"),
    description=load_instructions_file("agents/code_writer/description.txt"),
    tools=[write_to_file],
)
