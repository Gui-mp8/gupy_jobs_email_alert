import json

def load_config():
    with open('../config.json', 'r') as file:
        config_data = json.load(file)
    return config_data