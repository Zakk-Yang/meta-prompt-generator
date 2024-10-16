"""
Meta Prompt Generator

This package provides functionality to generate detailed system prompts
for language models based on task descriptions or existing prompts.
"""

from .generator import generate_prompt
from .prompts import META_PROMPT

__all__ = ["generate_prompt", "META_PROMPT"]
__version__ = "0.1.0"
