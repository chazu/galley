"""
Package: galley
Filename: config_file.py
Author(s): C Straney

A class representing the configuration for the current execution.
"""

# Python imports

# Our imports

# Third-party imports
import yaml


class Configuration:
    """Represents the configuration for the current execution"""

    def __init__(self, data):
        self.data = data

    @classmethod
    def load_from_file(cls, path):
        with open(path, 'r') as stream:
            try:
                return cls(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)
