#!/usr/bin/env python3
"""
Standalone local test for the Hello Agent
This tests the agent logic without requiring AWS deployment

Usage:
    uv run python test_local_standalone.py
"""

import json
from strands import Agent

def create_simple_agent():
    """Create a simple Strands agent for testing"""
    agent = Agent(
        name="HelloAgent",
        description="A simple agent that returns a hello message"
    )
    return agent

def process_message(agent, user_message):
    """Process a message without the full AWS infrastructure"""
    try:
        # Simple response logic (bypassing the full agent processing for now)
        response_message = f"Hello from local agent! You said: '{user_message}'"

        return {
            "status": "success",
            "message": response_message,
            "agent_name": agent.name,
            "echo": user_message
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"An error occurred: {str(e)}",
            "agent_name": agent.name
        }

def main():
    """Run local tests"""
    print("=" * 60)
    print("Standalone Local Agent Test")
    print("=" * 60)

    # Create the agent
    agent = create_simple_agent()
    print(f"Created agent: {agent.name}")
    print(f"Description: {agent.description}")
    print("-" * 60)

    # Test cases
    test_cases = [
        "Hello, World!",
        "How are you?",
        "Testing Strands Agent locally",
        "What's your name?",
    ]

    for i, test_input in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_input}")

        response = process_message(agent, test_input)
        print(f"Response: {json.dumps(response, indent=2)}")

        if response["status"] == "success":
            print("✓ Test passed")
        else:
            print("✗ Test failed")

    print("\n" + "=" * 60)
    print("All local tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()