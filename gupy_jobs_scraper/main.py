from utils.config import load_config
from scraper.etl import Etl
from scraper.send_email import SendEmail

from typing import Dict, List, Any

def main(config: Dict[str,Any]) -> List[Dict[str,Any]]:
    json_data = Etl(config).etl_result()
    return SendEmail(config).send_email(json_data)

if __name__ == "__main__":
    config = load_config()
    main(config)