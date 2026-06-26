from google.adk.agents import LlmAgent
from utils.file_loader import load_instructions_file

requirements_writer_agent = LlmAgent(
    name="requirements_writer_agents",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/requirements_writer/instructions.txt"),
    description=load_instructions_file("agents/requirements_writer/description.txt"),
    output_key="requirements_writer_output",
)
 