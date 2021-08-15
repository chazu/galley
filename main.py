"""
Package: N/A
Filename: main.py
Author(s): C. Straney

Entrypoint for the executable
"""

# Python imports
import argparse
from pathlib import Path

# Our imports
from galley import Configuration, AggregatedYaml, ResourceMapping, Resource

# Third-party imports
import yaml


DEKOMPOSE_DESCRIPTION = """
A utility for managing manifests of kubernetes projects
 distributed as single YAML files.
"""

def map_resources(aggregated, existing):
    result = {
        "mappings": [],
        "unmapped": []
    }

    for agg in aggregated:
        for resource in existing:
            if agg.matches(resource):
                rmap = ResourceMapping(agg, resource)
                result['mappings'].append(rmap)
                continue
        result['unmapped'].append(agg)

    return result

def write_resource_to_file(resource, path):
    filename = f"{resource.data['kind']}.yaml"
    with open(f"{path}/{filename}", 'w') as file:
        yaml.dump(resource.data, file)

if __name__ == "__main__":
    existing_resources = []
    new_resources = []

    parser = argparse.ArgumentParser(description=DEKOMPOSE_DESCRIPTION)

    parser.add_argument('-f', '--config-file',
                        default="./galley.yaml",
                        dest="configfile",
                        help='path to config file (default dekompose.yaml')
    args = parser.parse_args()

    config = Configuration.load_from_file(args.configfile)

    # Get resources from the aggregated manifest
    aggregated_yaml = AggregatedYaml(config.data['sourceYaml'])
    aggregate_resources = aggregated_yaml.resources

    # Get existing resources
    for path in Path(config.data['destinationFolder']).rglob('*.yaml'):
        with open(path, 'r') as stream:
            try:
                res = Resource(yaml.safe_load(stream), path, False)
                existing_resources.append(res)
            except yaml.YAMLError as exc:
                print(exc)

    # Create mappings
    mappings = map_resources(aggregate_resources, existing_resources)
    import pdb; pdb.set_trace()
    # Write out files for unmapped resources
    for x in mappings['unmapped']:
        write_resource_to_file(x, config.data['destinationFolder'])
