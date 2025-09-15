#!/usr/bin/env python3
"""
AWS Bedrock AgentCore Deployment Test Script
Tests the deployed Hello Agent on AWS

Usage:
    uv run python test_deployment.py --agent-arn <AGENT_ARN>
    uv run python test_deployment.py  # Uses ARN from .agent_arn file if exists
"""

import argparse
import json
import sys
import os
import time
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def load_saved_arn():
    """Try to load saved Agent ARN from file"""
    arn_file = ".agent_arn"
    if os.path.exists(arn_file):
        with open(arn_file, 'r') as f:
            return f.read().strip()
    return None

def test_deployed_agent(agent_arn, session_id=None):
    """Test the deployed agent on AWS Bedrock AgentCore"""

    print("=" * 60)
    print("Testing Deployed Agent on AWS Bedrock AgentCore")
    print("=" * 60)
    print(f"Agent ARN: {agent_arn}")

    # Generate session ID if not provided
    if not session_id:
        session_id = f"test-session-{int(time.time())}"
    print(f"Session ID: {session_id}")
    print("-" * 60)

    try:
        # Initialize the Bedrock AgentCore client
        client = boto3.client('bedrock-agentcore', region_name='us-east-1')

        # Test cases
        test_cases = [
            {"prompt": "Hello, World!"},
            {"prompt": "How are you?"},
            {"prompt": "Testing AWS Bedrock Agent"},
            {"prompt": "What's your name?"},
        ]

        for i, test_payload in enumerate(test_cases, 1):
            print(f"\nTest Case {i}:")
            print(f"Input: {test_payload}")

            try:
                # Prepare the payload
                payload = json.dumps(test_payload).encode()

                # Invoke the agent
                response = client.invoke_agent_runtime(
                    agentRuntimeArn=agent_arn,
                    runtimeSessionId=session_id,
                    payload=payload
                )

                # Process response
                if 'payload' in response:
                    result = json.loads(response['payload'])
                    print(f"Response: {json.dumps(result, indent=2)}")

                    # Verify response structure
                    if "status" in result and result["status"] == "success":
                        print("✓ Test passed")
                    else:
                        print("✗ Test returned error status")
                else:
                    print("✗ No payload in response")

            except ClientError as e:
                error_code = e.response['Error']['Code']
                error_message = e.response['Error']['Message']
                print(f"✗ AWS API Error: {error_code} - {error_message}")

                if error_code == 'ResourceNotFoundException':
                    print("  Agent not found. Please check the ARN.")
                elif error_code == 'AccessDeniedException':
                    print("  Access denied. Check your AWS permissions.")

            except Exception as e:
                print(f"✗ Test failed: {str(e)}")

        print("\n" + "=" * 60)
        print("Testing Complete!")
        print("=" * 60)

    except NoCredentialsError:
        print("✗ AWS credentials not found. Please configure AWS CLI.")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Failed to initialize AWS client: {str(e)}")
        sys.exit(1)

def invoke_via_cli(prompt):
    """Alternative method using agentcore CLI"""
    print("\nAlternative: Testing via AgentCore CLI")
    print("-" * 40)

    payload = json.dumps({"prompt": prompt})
    cmd = f"uv run agentcore invoke '{payload}'"

    print(f"Command: {cmd}")
    print("Run this command manually to test your agent")

def main():
    parser = argparse.ArgumentParser(
        description='Test deployed Hello Agent on AWS Bedrock AgentCore'
    )
    parser.add_argument(
        '--agent-arn',
        type=str,
        help='Agent Runtime ARN (e.g., arn:aws:bedrock-agentcore:region:account:agent-runtime/name)'
    )
    parser.add_argument(
        '--session-id',
        type=str,
        help='Runtime session ID (optional, will generate if not provided)'
    )
    parser.add_argument(
        '--prompt',
        type=str,
        default="Hello from test script!",
        help='Custom prompt to test with'
    )
    parser.add_argument(
        '--cli-only',
        action='store_true',
        help='Only show CLI command, don\'t run API test'
    )

    args = parser.parse_args()

    # Try to get agent ARN
    agent_arn = args.agent_arn
    if not agent_arn:
        agent_arn = load_saved_arn()
        if agent_arn:
            print(f"Using saved Agent ARN from .agent_arn file")
        else:
            print("Error: No agent ARN provided and no .agent_arn file found")
            print("Usage: python test_deployment.py --agent-arn <AGENT_ARN>")
            print("Or run ./deploy.sh first to save the ARN automatically")
            sys.exit(1)

    if args.cli_only:
        invoke_via_cli(args.prompt)
    else:
        test_deployed_agent(agent_arn, args.session_id)
        print("\n" + "-" * 60)
        invoke_via_cli(args.prompt)

if __name__ == "__main__":
    main()