from google.adk.agents import SequentialAgent
from agents.requirements_writer import requirements_writer_agent
from agents.designer import designer_agent
from agents.code_writer import code_writer_agent
from utils.file_loader import load_instructions_file

root_agent = SequentialAgent(
    name="root_website_builder_agent",
    sub_agents=[requirements_writer_agent, designer_agent, code_writer_agent],
    description=load_instructions_file("agents/root_website_builder/description.txt"),
)