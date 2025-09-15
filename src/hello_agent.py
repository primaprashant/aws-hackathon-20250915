"""
Simple Hello World Agent for AWS Bedrock AgentCore deployment
This agent demonstrates the minimal setup needed to deploy with Strands and AWS Bedrock
"""

from strands import Agent
from bedrock_agentcore.runtime import BedrockAgentCoreApp


from strands.models import BedrockModel

SYSTEM_PROMPT = """You are a helpful marketer assistant.
Your role is to:
- Research competitors similar to the idea given by the user
- Provide a comprehensive Vision Document for the idea

You have access to the following tools:
1. web_search() - To access current technical documentation, or for updated information.

Always use the appropriate tool to get accurate, up-to-date information rather than making assumptions about electronic products or specifications."""

# Initialize the Bedrock model (Anthropic Claude 3.7 Sonnet)
model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    temperature=0.3,
    region_name='us-west-2',
)

# Create the customer support agent with all tools
agent = Agent(
    name="HelloAgent",
    model=model,
    # tools=[
    #     web_search, # Tool 3: Access the web for updated information
    # ],
    system_prompt=SYSTEM_PROMPT,
)

print("Hello Agent created successfully!")

# Initialize the Bedrock AgentCore app
app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    """
    Process user input and return a response

    Args:
        payload: Dictionary containing the request data
            - prompt: The user's input message

    Returns:
        JSON-serializable response
    """
    # Extract the user message from payload
    user_message = payload.get("prompt", "You should ask a question bro!")

    # Process the message through the agent
    try:
        # For this simple example, we'll just return a greeting
        # In a real scenario, the agent would process the message
        response_message = agent(user_message)

        # Return a structured response
        return {
            "status": "success",
            "message": response_message,
            "agent_name": agent.name,
            "echo": user_message
        }
    except Exception as e:
        # Handle any errors gracefully
        return {
            "status": "error",
            "message": f"An error occurred: {str(e)}",
            "agent_name": agent.name
        }

# For local testing
if __name__ == "__main__":
    # Run the app locally for testing
    print("Starting Hello Agent locally...")
    app.run()