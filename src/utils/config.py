import json
from typing import Dict, Any

def load_config() -> Dict[str,Any]:
    with open('config.json', 'r') as file:
        config_data = json.load(file)
    return config_data