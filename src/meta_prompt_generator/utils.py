"""
This module contains utility functions for the meta prompt generator.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_api_key(api_key: Optional[str] = None) -> str:
    """
    Get the OpenAI API key from the provided argument, environment variable, or .env file.

    Args:
        api_key (Optional[str]): The API key provided as an argument.

    Returns:
        str: The OpenAI API key.

    Raises:
        ValueError: If no API key is found.
    """
    if api_key:
        return api_key

    env_api_key = os.getenv("OPENAI_API_KEY")
    if env_api_key:
        return env_api_key

    raise ValueError(
        "No OpenAI API key provided. Please provide it as an argument, set the OPENAI_API_KEY environment variable, or include it in a .env file."
    )


def format_markdown(content: str) -> str:
    """
    Format the content as a markdown code block.

    Args:
        content (str): The content to format.

    Returns:
        str: The content wrapped in markdown code blocks.
    """
    return f"```markdown\n{content}\n```"
