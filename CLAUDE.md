# Project Rules
- /src will be the working directory

## Package Management
- Always use `uv` for package management
- Run Python scripts with `uv run python <script.py>`

## AWS Bedrock Agent Development
- Use `strands` library for agent creation
- Use `BedrockModel` from strands for AWS Bedrock integration
- Model ID: `anthropic.claude-3-5-sonnet-20241022-v2:0`
- Always load AWS credentials from `.env` file using `python-dotenv`

## Code Structure
- Keep agent code simple and direct
- Use boto3 session with explicit credentials
- Handle both direct execution and interactive modes
- Minimal error handling - fail fast with clear messages