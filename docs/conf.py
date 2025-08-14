import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Math Project'
author = 'Ganesh'
release = '1.0'

extensions = [
    'sphinx_needs',
]

needs_types = [
    dict(directive='req', title='Requirement', prefix='REQ_'),
    dict(directive='spec', title='Specification', prefix='SPEC_'),
    dict(directive='test', title='Test Case', prefix='TEST_'),
]

needs_extra_options = [
    'author'
]

html_theme = 'alabaster'
