"""
This module contains the main functionality for generating prompts.
"""

import logging
from typing import Optional

from openai import OpenAI
from openai import OpenAIError
import json

from .prompts import META_PROMPT, META_SCHEMA, META_SCHEMA_PROMPT
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


class SchemaGenerationError(Exception):
    """Custom exception for schema generation errors."""

    pass


def generate_meta_schema(
    task_or_prompt: str,
    api_key: Optional[str] = None,
    schema_template: dict = META_SCHEMA,
    prompt_template: Optional[str] = META_SCHEMA_PROMPT,
    model_name: Optional[str] = "gpt-4o-mini",
) -> dict:
    """
    Generate a JSON schema based on a task description or prompt.

    Args:
        task_or_prompt (str): The task description or prompt for which to generate a schema.
        api_key (Optional[str]): OpenAI API key. If not provided, it will use the default from environment variables.
        schema_template (dict): The base schema template to use. Defaults to META_SCHEMA.
        prompt_template (Optional[str]): The prompt template to use. Defaults to META_SCHEMA_PROMPT.
        model_name (Optional[str]): The OpenAI model to use. Defaults to "gpt-4o-mini".

    Returns:
        dict: The generated JSON schema.

    Raises:
        SchemaGenerationError: If there's an error during schema generation.
    """
    try:
        api_key = get_api_key(api_key=api_key)
        client = OpenAI(api_key=api_key)

        logger.info(
            "Generating schema for task/prompt: %s",
            task_or_prompt[:50] + "..." if len(task_or_prompt) > 50 else task_or_prompt,
        )

        completion = client.chat.completions.create(
            model=model_name,
            response_format={"type": "json_schema", "json_schema": schema_template},
            messages=[
                {
                    "role": "system",
                    "content": prompt_template,
                },
                {
                    "role": "user",
                    "content": f"Task or Prompt:\n{task_or_prompt}",
                },
            ],
        )

        schema = json.loads(completion.choices[0].message.content)
        logger.info("Schema generated successfully")

        return schema

    except OpenAIError as e:
        logger.error("OpenAI API error: %s", str(e))
        raise SchemaGenerationError(f"Error in OpenAI API call: {str(e)}") from e
    except json.JSONDecodeError as e:
        logger.error("JSON decoding error: %s", str(e))
        raise SchemaGenerationError(f"Error decoding JSON response: {str(e)}") from e
    except Exception as e:
        logger.error("Unexpected error: %s", str(e))
        raise SchemaGenerationError(
            f"Unexpected error during schema generation: {str(e)}"
        ) from e
