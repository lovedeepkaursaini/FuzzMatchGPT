from setuptools import setup, find_packages

setup(
    name="FuzzMatchGPT",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'openai',
        'scikit-learn',
        'pandas',
    ],
)
