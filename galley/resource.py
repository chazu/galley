"""
Package: galley
Filename: resource.py
Author(s): C Straney

A class that represents a resource from a particular file
"""

# Python imports

# Our imports

# Third-party imports


class Resource:

    def __init__(self, data, filepath: str, aggregated: bool):
        """
        Create a resource instance.

        data - the yaml document returned when the file was parsed
        filepath - the path to the file from which this resource was read
        aggregated - whether the source file was an aggregate manifest
        """
        self.data = data
        self.filepath = filepath
        self.aggregated = aggregated

    def kind(self) -> str:
        return self.data['kind']

    def name(self) -> str:
        return self.data['metadata']['name']

    def matches(self, other) -> bool:

        """Returns true if the resources are deemed to be equivalent"""
        return self.kind() == other.kind() and self.name() == other.name()
