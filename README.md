# Meta Prompt Generator

Meta Prompt Generator is a Python package that generates detailed system prompts for language models based on task descriptions or existing prompts. It leverages OpenAI's GPT models to create well-structured, task-specific prompts that can be used to guide AI models in completing various tasks effectively. You can also use it in cli. 

## Features

- Generate detailed system prompts from task descriptions
- Flexible API key management (via argument or environment variable)
- Option to output prompts with or without markdown formatting
- Robust error handling and logging

## Installation

To install the Meta Prompt Generator, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/Zakk-Yang/meta-prompt-generator.git
   cd meta-prompt-generator
   ```

2. Install the package in editable mode with development dependencies:
   ```
   pip install meta-prompt-generator
   ```

## Usage

Here's a basic example of how to use the Meta Prompt Generator:

```python
from meta_prompt_generator import generate_prompt

# Generate a prompt
task = "Create a prompt for generating creative short stories"
prompt = generate_prompt(task)

print(prompt)
```

The generated prompt is wrapped in markdown code blocks.

Use in cli:
```bash
meta-prompt "Create a prompt for generating creative short stories"
```

### API Key

The package requires an OpenAI API key. You can provide it in two ways:

1. As an argument to the `generate_prompt` function:
   ```python
   prompt = generate_prompt(task, api_key="your-api-key-here")
   ```

2. As an environment variable named `OPENAI_API_KEY`:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
3. Create .env in the root to include 
```
OPENAI_API_KEY = 'sk-xxx'
```
Note: Make sure to add .env to your .gitignore file to avoid accidentally committing your API key.


## Contributing

Contributions to the Meta Prompt Generator are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the OpenAI API to generate prompts.
- Thanks to all contributors who have helped shape this project.

