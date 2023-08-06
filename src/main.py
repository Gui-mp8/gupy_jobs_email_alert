from utils.config import load_config
from scraper.web_scraper import WebScraper
from transformation.transformation import Transform
from send_email.send_email import SendEmail

from typing import Dict, List, Any

def main(config: Dict[str,Any]) -> List[Dict[str,Any]]:
    data = WebScraper(config).extract_data_to_json()
    json_data = Transform(json_data=data).data_filter()
    return SendEmail(config, json_data).send_email()

if __name__ == "__main__":
    config = load_config()
    main(config)