import json


def load_index() -> dict:

    with open(pkg_resources.resource_filename("data/pos_index.json"), 'r') as f:
        positional_index = json.load(f)
        
    return positional_index
