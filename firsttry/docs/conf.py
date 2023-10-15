"""Sphinx configuration."""
project = "Firsttry"
author = "Evelyn  Mitchell"
copyright = "2023, Evelyn  Mitchell"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
