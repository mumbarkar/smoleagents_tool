# call libraries, classes, and methods
import os
from dotenv import load_dotenv
from smolagents import (
    load_tool,
    CodeAgent,
    InferenceClientModel,
    GradioUI
)

# Laod environment variables from .env file
load_dotenv()
# Get Hugging Face API key from environment variable
hf_api_key = os.getenv("HF_TOKEN")
model_id = "m-ric/text-to-image"

# Import tool from Hub
image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

# Initialize the model with the specified model_id
model = InferenceClientModel(token=hf_api_key, model_id=model_id)

# Initialize the agent with the image generation tool
agent = CodeAgent(tools=[image_generation_tool], model=model)

GradioUI(agent).launch()