"""
Package: galley
Filename: aggregated_yaml.py
Author(s): C Straney

A class representing the single file to be divided into manifests
"""

# Python imports

# Our imports
from .resource import Resource
# Third-party imports
import yaml

class AggregatedYaml:
    """Represents the single file which is to be divided into manifests"""

    def __init__(self, path):
        with open(path, 'r') as stream:
            documents = list(yaml.load_all(stream))
            self.resources = [Resource(x, path, True) for x in documents]
