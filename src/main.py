import time
from typing import Dict, List, Any

import asyncio

from utils.config import load_config
from scraper.web_scraper import WebScraper
from transformation.transformation import Transform
from validation.validation import DataValidator
from send_email.send_email import SendEmail

def main(config: Dict[str,Any]):
    data = asyncio.run(WebScraper(config).extract_data_to_json())
    list_dict_data = Transform(config, json_data=data).data_filter()
    validated_data = DataValidator.result_validation(list_dict_data=list_dict_data)

    return SendEmail(config, validated_data).send_email()

if __name__ == "__main__":
    start_time = time.time()
    config = load_config()
    main(config)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program execution time: {elapsed_time} seconds")
