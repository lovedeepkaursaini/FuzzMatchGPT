# Introduction
Data matching, the process of identifying similar records across multiple datasets, is a common challenge in data management. In this code, we will use a powerful approach to fuzzy data matching using GPT-based embeddings and Nearest Neighbors. 

# FuzzMatchGPT

FuzzMatchGPT is a Python library providing a utility for fuzzy matching records in pandas dataframes, using OpenAI's GPT for generating text embeddings and scikit-learn's Nearest Neighbors for finding the closest matches.

## Usage

Import the `fuzzy_match` function from the `FuzzyMatchGPT` module:

```python
from FuzzMatchGPT.FuzzyMatchGPT import fuzzy_match

