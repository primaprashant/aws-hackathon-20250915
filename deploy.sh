#!/bin/bash

# AWS Bedrock AgentCore Deployment Script
# This script helps deploy the Hello Agent to AWS Bedrock AgentCore
# Uses uv for dependency management

set -e  # Exit on error

echo "=========================================="
echo "AWS Bedrock AgentCore Deployment Script"
echo "=========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Check prerequisites
echo ""
echo "Checking prerequisites..."

# Check uv
if ! command -v uv &> /dev/null; then
    print_error "uv is not installed. Please install it first: https://github.com/astral-sh/uv"
    exit 1
else
    print_status "uv is installed: $(uv --version)"
fi

# Check Python version
if ! uv run python --version &> /dev/null; then
    print_error "Python is not available through uv"
    exit 1
else
    print_status "Python is available: $(uv run python --version)"
fi

# Check AWS CLI
if ! aws --version &> /dev/null; then
    print_error "AWS CLI is not installed"
    exit 1
else
    print_status "AWS CLI is installed: $(aws --version)"
fi

# Sync dependencies
echo ""
echo "Syncing dependencies with uv..."
uv sync
if [ $? -eq 0 ]; then
    print_status "Dependencies synced successfully"
else
    print_error "Failed to sync dependencies"
    exit 1
fi

# Configure the agent
echo ""
echo "Configuring agent for deployment..."
uv run agentcore configure --entrypoint src/hello_agent.py
if [ $? -eq 0 ]; then
    print_status "Agent configured successfully"
else
    print_error "Failed to configure agent"
    exit 1
fi


# Deploy to AWS
uv run agentcore launch
