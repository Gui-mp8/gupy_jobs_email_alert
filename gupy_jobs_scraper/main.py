from utils.config import load_config
from scraper.modules.web_scraper import WebScraper

def main(config):
    return print(WebScraper(config).extract_data_to_json())

if __name__ == "__main__":
    config = load_config()
    main(config)