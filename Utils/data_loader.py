import json

def load_json_data(path):
    with open(path, 'r') as f:
        return json.load(f)