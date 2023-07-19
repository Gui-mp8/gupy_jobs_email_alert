from utils.config import load_config
from scraper.etl import Etl
from typing import Dict, List, Any

def main(config: Dict[str,Any]) -> List[Dict[str,Any]]:
    return print(Etl(config).etl_result())

if __name__ == "__main__":
    config = load_config()
    main(config)