from agents.root_website_builder.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name="website_builder",
    session_service=session_service
)

print("Runner created successfully")