from utils.config import load_config
from scraper.web_scraper import WebScraper
from transformation.transformation import Transform
from validation.validation import DataValidator
from send_email.send_email import SendEmail

from typing import Dict, List, Any

def main(config: Dict[str,Any]) -> List[Dict[str,Any]]:
    data = WebScraper(config).extract_data_to_json()
    list_dict_data = Transform(config, json_data=data).data_filter()
    validated_data = DataValidator.result_validation(list_dict_data=list_dict_data)

    return SendEmail(config, validated_data).send_email()

if __name__ == "__main__":
    config = load_config()
    main(config)