#!/usr/bin/env python3
"""
Local testing script for the Hello Agent
Run this script to test the agent locally before AWS deployment

Usage:
    uv run python test_local.py
"""

import sys
import json
from src.hello_agent import invoke

def test_agent():
    """Test the agent with various inputs"""
    print("=" * 60)
    print("Testing Hello Agent Locally")
    print("=" * 60)

    # Test cases
    test_cases = [
        {"prompt": "Hello, World!"},
        {"prompt": "How are you?"},
        {"prompt": "Testing AWS Bedrock Agent"},
        {},  # Test default behavior
    ]

    for i, test_payload in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_payload}")

        try:
            response = invoke(test_payload)
            print(f"Response: {json.dumps(response, indent=2)}")

            # Verify response structure
            assert "status" in response, "Response missing 'status' field"
            assert "message" in response, "Response missing 'message' field"
            assert "agent_name" in response, "Response missing 'agent_name' field"

            if response["status"] == "success":
                print("✓ Test passed")
            else:
                print("✗ Test resulted in error response")

        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            sys.exit(1)

    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    test_agent()