# Meta Prompt Generator

Meta Prompt Generator is a Python package that generates detailed system prompts for language models based on task descriptions or existing prompts. It leverages OpenAI's GPT models to create well-structured, task-specific prompts that can be used to guide AI models in completing various tasks effectively. You can also use it in cli. 

## Features

- Generate detailed system prompts from task descriptions in just one line of code
- Flexible API key management (via argument or environment variable)
- Robust error handling and logging

## Installation

To install the Meta Prompt Generator, you can either clone or use pip:

1. Clone the repository:
   ```
   git clone https://github.com/Zakk-Yang/meta-prompt-generator.git
   cd meta-prompt-generator
   ```

2. Install the package through pip:
   ```
   pip install meta-prompt-generator --upgrade
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

Before customizing your own template, it is recommended to check the current template.

```python
from  meta_prompt_generator.prompts import META_PROMPT
print(META_PROMPT)
```
Output:
```markdown
Given a task description or existing prompt, produce a detailed system prompt to guide a language model in completing the task effectively.

# Guidelines

- Understand the Task: Grasp the main objective, goals, requirements, constraints, and expected output.
- Minimal Changes: If an existing prompt is provided, improve it only if it's simple. For complex prompts, enhance clarity and add missing elements without altering the original structure.
- Reasoning Before Conclusions: Encourage reasoning steps before any conclusions are reached. ATTENTION! If the user provides examples where the reasoning happens afterward, REVERSE the order! NEVER START EXAMPLES WITH CONCLUSIONS!
    - Reasoning Order: Call out reasoning portions of the prompt and conclusion parts (specific fields by name). For each, determine the ORDER in which this is done, and whether it needs to be reversed.
    - Conclusion, classifications, or results should ALWAYS appear last.
- Examples: Include high-quality examples if helpful, using placeholders [in brackets] for complex elements.
   - What kinds of examples may need to be included, how many, and whether they are complex enough to benefit from placeholders.
- Clarity and Conciseness: Use clear, specific language. Avoid unnecessary instructions or bland statements.
- Formatting: Use markdown features for readability. DO NOT USE ``` CODE BLOCKS UNLESS SPECIFICALLY REQUESTED.
- Preserve User Content: If the input task or prompt includes extensive guidelines or examples, preserve them entirely, or as closely as possible. If they are vague, consider breaking down into sub-steps. Keep any details, guidelines, examples, variables, or placeholders provided by the user.
- Constants: DO include constants in the prompt, as they are not susceptible to prompt injection. Such as guides, rubrics, and examples.
- Output Format: Explicitly the most appropriate output format, in detail. This should include length and syntax (e.g. short sentence, paragraph, JSON, etc.)
    - For tasks outputting well-defined or structured data (classification, JSON, etc.) bias toward outputting a JSON.
    - JSON should never be wrapped in code blocks (```) unless explicitly requested.

The final prompt you output should adhere to the following structure below. Do not include any additional commentary, only output the completed system prompt. SPECIFICALLY, do not include any additional messages at the start or end of the prompt. (e.g. no "---")

[Concise instruction describing the task - this should be the first line in the prompt, no section header]

[Additional details as needed.]

[Optional sections with headings or bullet points for detailed steps.]

# Steps [optional]

[optional: a detailed breakdown of the steps necessary to accomplish the task]

# Output Format

[Specifically call out how the output should be formatted, be it response length, structure e.g. JSON, markdown, etc]

# Examples [optional]

[Optional: 1-3 well-defined examples with placeholders if necessary. Clearly mark where examples start and end, and what the input and output are. User placeholders as necessary.]
[If the examples are shorter than what a realistic example is expected to be, make a reference with () explaining how real examples should be longer / shorter / different. AND USE PLACEHOLDERS! ]

# Notes [optional]

[optional: edge cases, details, and an area to call or repeat out specific important considerations]

```


Then, you can change your own template and apply:
```python
my_meta_prompt = """ Customize your own template here """
task = "Create a prompt for generating creative short stories"
prompt = generate_prompt(task, prompt_template = my_meta_prompt)
print(prompt)
```

Output in json format:
You chan check the schema template first:
```python
from  meta_prompt_generator.prompts import META_SCHEMA_PROMPT, META_SCHEMA
print(META_SCHEMA_PROMPT)
print(META_SCHEMA)
```
Create json output:
```python
from meta_prompt_generator.generator import generate_meta_schema
print(generate_meta_schema('generate KPIs for a data team'))
```
Output:
```json
{
  "name": "kpis_data_team",
  "type": "object",
  "properties": {
    "kpi_list": {
      "type": "array",
      "description": "A list of KPIs defined for the data team.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the KPI."
          },
          "description": {
            "type": "string",
            "description": "A brief description of what the KPI measures."
          },
          "target": {
            "type": "string",
            "description": "The target value or goal for the KPI."
          },
          "frequency": {
            "type": "string",
            "description": "The frequency of measuring this KPI (e.g., weekly, monthly)."
          },
          "owner": {
            "type": "string",
            "description": "The individual or role responsible for this KPI."
          }
        },
        "required": [
          "name",
          "description",
          "target",
          "frequency",
          "owner"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "kpi_list"
  ],
  "additionalProperties": false
}
```
Feel free to change both `META_SCHEMA_PROMPT` and `META_SCHEMA` or other parameters by the example below:
    task_or_prompt: str,
    api_key: Optional[str] = None,
    schema_template: dict = META_SCHEMA,
    prompt_template: Optional[str] = META_SCHEMA_PROMPT,
    model_name: Optional[str] = "gpt-4o-mini",
```python
from meta_prompt_generator.generator import generate_meta_schema
print(generate_meta_schema(task_or_prompt = 'generate KPIs for a data team',
                           schema_template = 'your schema template',
                           prompt_template = 'your prompt template',
                           model_name = 'your preferred openai model name' # default is gpt-4o-mini
                            ))
```

Use in cli:

By default, it is using the `gpt-4o-mini` model.
```bash
meta-prompt "Create a prompt for generating creative short stories"
```

You can choose to use a different model.
```bash
meta-prompt "Design a system to classify customer feedback" --model-name gpt-4o
```
It is not recommended to add your customized prompt template here as it can be very lengthy. 

### API Key

The package requires an OpenAI API key. You can provide it in three ways:

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

