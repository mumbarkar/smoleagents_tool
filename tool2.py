# This file is part of smoleagents_tool, a tool for building and running agents.

# call libraries, classes, and methods
import os
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool

# Laod environment variables from .env file
load_dotenv()

# Get Hugging Face API key from environment variable
hf_api_key = os.getenv("HF_TOKEN")

# Initialize a model (using Higging FAce Inference API)
model = InferenceClientModel(token=hf_api_key)

# Create an agent with DuckDuckGoSearch tool (Agent Initialization)
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model = model)

# Run the agent with a prompt
response = agent.run("What is the current weather in Hyderabad?")
print(response)