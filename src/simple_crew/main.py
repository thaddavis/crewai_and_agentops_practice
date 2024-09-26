from src.simple_crew.crew import SimpleCrew
from dotenv import load_dotenv
import os
import agentops

load_dotenv()

agentops.init(os.getenv("AGENTOPS_API_KEY"), default_tags=["Revolutionary War"])

print("Running SimpleCrew...")
SimpleCrew().crew().kickoff()