import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'Sphinx-Needs Demo'
author = 'Ganesh'
release = '1.0'

extensions = [
    'sphinx_needs',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
