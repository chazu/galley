"""
Package: galley
Filename: resource_mapping.py
Author(s): C Straney

A class representing a mapping from one resource to another
"""

# Python imports

# Our imports

# Third-party imports

class ResourceMapping:
    """A (directional) mapping between two resource instances"""

    def __init__(self, origin_resource, destination_resource):
        self.origin = origin_resource
        self.destination = destination_resource
