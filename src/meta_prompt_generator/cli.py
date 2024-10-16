import argparse
from .generator import generate_prompt


def main():
    parser = argparse.ArgumentParser(description="Generate a meta prompt.")
    parser.add_argument(
        "task", type=str, help="The task description or existing prompt"
    )
    args = parser.parse_args()

    prompt = generate_prompt(args.task)
    print(prompt)


if __name__ == "__main__":
    main()
