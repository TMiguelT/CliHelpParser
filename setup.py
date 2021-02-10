#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    packages=find_packages(exclude="test"),
    install_requires=[
        "pyparsing",
        "jinja2",
        "spacy ~= 3.0",
        "miniwdl",
        "wordsegment",
        "inflection",
        "illusional.wdlgen==0.3.0",
        "ruamel.yaml==0.16.5",
        "click",
        "cwltool",
        "cwl-utils>=0.4",
        "regex",
        "num2words",
        "word2number",
        "psutil",
        "deprecated",
        "attrs",
        "janis-pipelines.core >= 0.11.2",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["aclimatise = aclimatise.cli:main"]},
    extras_require={
        "dev": [
            "pytest",
            "pre-commit",
            "Sphinx",
            "sphinx-click",
            "pytest-timeout",
            "docker",
        ],
    },
)
