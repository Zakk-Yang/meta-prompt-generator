"""
This module contains the main functionality for generating prompts.
"""

import logging
from typing import Optional

from openai import OpenAI
from openai import OpenAIError

from .prompts import META_PROMPT
from .utils import get_api_key, format_markdown

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PromptGenerationError(Exception):
    """Custom exception for prompt generation errors."""

    pass


def generate_prompt(
    task_or_prompt: str,
    api_key: Optional[str] = None,
    prompt_template: Optional[str] = META_PROMPT,
    model_name: Optional[str] = "gpt-4o-mini",
) -> str:
    """
    Generate a detailed system prompt based on a task description or existing prompt.

    Args:
        task_or_prompt (str): The task description or existing prompt.
        api_key (Optional[str]): OpenAI API key. If not provided, it will use the default from environment variables.
        prompt_template (Optional[str]): by default, this template comes from openai's Prompt generation documentation.
        model_name (Optional[str]): by default it isgpt-4o-mini, replace your preferred openai model
    Returns:
        str: The generated prompt wrapped in markdown code blocks.

    Raises:
        PromptGenerationError: If there's an error during prompt generation.
    """
    try:
        api_key = get_api_key(api_key=api_key)
        client = OpenAI(api_key=api_key)

        logger.info(
            "Generating prompt for task: %s",
            task_or_prompt[:50] + "..." if len(task_or_prompt) > 50 else task_or_prompt,
        )

        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": prompt_template,
                },
                {
                    "role": "user",
                    "content": f"Task, Goal, or Current Prompt:\n{task_or_prompt}",
                },
            ],
        )

        response = completion.choices[0].message.content
        logger.info("Prompt generated successfully")

        return format_markdown(response)

    except OpenAIError as e:
        logger.error("OpenAI API error: %s", str(e))
        raise PromptGenerationError(f"Error in OpenAI API call: {str(e)}") from e
    except Exception as e:
        logger.error("Unexpected error: %s", str(e))
        raise PromptGenerationError(
            f"Unexpected error during prompt generation: {str(e)}"
        ) from e
