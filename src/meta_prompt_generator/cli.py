import argparse
from .generator import generate_prompt


def main():
    parser = argparse.ArgumentParser(description="Generate a meta prompt.")
    parser.add_argument(
        "task", type=str, help="The task description or existing prompt"
    )
    parser.add_argument(
        "model_name",
        type=str,
        help="The name of the model to use (e.g., 'gpt-3.5-turbo', 'gpt-4o-mini')",
    )

    args = parser.parse_args()

    prompt = generate_prompt(task_or_prompt=args.task, model_name=args.model_name)
    print(prompt)


if __name__ == "__main__":
    main()
