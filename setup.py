import os
from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


# Read the contents of your requirements file
def read_requirements():
    with open("requirements.txt") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


requirements = read_requirements()

setup(
    name="meta-prompt-generator",
    version="0.1.4",
    author="Zakk Yang",
    author_email="zakkyang@hotmail.com",
    description="A package to generate step-by-step reasoning prompts for language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zakk-Yang/meta-prompt-generator.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "meta-prompt=meta_prompt_generator.cli:main",
        ],
    },
)
