"""
Simple Hello World Agent for AWS Bedrock AgentCore deployment
This agent demonstrates the minimal setup needed to deploy with Strands and AWS Bedrock
"""

from strands import Agent
from bedrock_agentcore.runtime import BedrockAgentCoreApp

# Initialize the Strands agent
agent = Agent(
    name="HelloAgent",
    description="A simple agent that returns a hello message"
)

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
    user_message = payload.get("prompt", "Hello")

    # Process the message through the agent
    try:
        # For this simple example, we'll just return a greeting
        # In a real scenario, the agent would process the message
        response_message = f"Hello from AWS Bedrock Agent! You said: '{user_message}'"

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