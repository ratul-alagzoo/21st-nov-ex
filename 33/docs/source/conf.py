import os
import sys
# Configuration file for the Sphinx documentation builder.
#
sys.path.insert(0, os.path.abspath("../../src"))
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'my_test-pkg_docs'
copyright = '2025, anik'
author = 'anik'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # MyST Markdown support
    "sphinx.ext.autodoc",  # Auto API docs from docstrings
    "sphinx.ext.napoleon",  # NumPy / Google style docstrings
]

templates_path = ['_templates']
# Allow both reStructuredText and Markdown source files
source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}

# Sphinx 4+ uses `root_doc` (replaces master_doc)
root_doc = 'index'

# Common excludes
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# MyST-Parser optional settings
myst_enable_extensions = [
    "colon_fence",
]
myst_heading_anchors = 3



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Napoleon configuration (both styles on)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_param = True
napoleon_use_rtype = True
