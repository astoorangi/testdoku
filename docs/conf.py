import sys, os

master_doc = 'index'
sys.path.append(os.path.abspath('sphinxext'))
extensions = [
    'sphinxcontrib.versioning.sphinx_',
]

