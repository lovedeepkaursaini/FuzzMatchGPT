# Introduction
Data matching, the process of identifying similar records across multiple datasets, is a common challenge in data management. In this code, we will use a powerful approach to fuzzy data matching using GPT-based embeddings and Nearest Neighbors. 

# FuzzMatchGPT

FuzzMatchGPT is a Python library providing a utility for fuzzy matching records in pandas dataframes, using OpenAI's GPT for generating text embeddings and scikit-learn's Nearest Neighbors for finding the closest matches.

## Usage

Import the `fuzzy_match` function from the `FuzzyMatchGPT` module:

```python
from FuzzMatchGPT.FuzzyMatchGPT import fuzzy_match
```

## Setup

This package uses the OpenAI API, and you will need an OpenAI API key to use it. Please obtain an API key from OpenAI.

Once you have the key, set it as an environment variable. The package will read the key from this environment variable.

If you're using a Unix-like operating system, open your `.bashrc` or `.zshrc` file and add the following line:

```export OPENAI_API_KEY='your-openai-api-key'```


Then, restart your terminal or run `source ~/.bashrc` (or `source ~/.zshrc`).

If you're using Windows, you can add a new environment variable in the System Properties. The exact steps may vary depending on your version of Windows.

Then in your Python code, you can access this key as you're currently doing:

```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
```
