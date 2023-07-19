from utils.config import load_config
from scraper.etl import Etl

def main(config):
    return print(Etl(config).etl_result())

if __name__ == "__main__":
    config = load_config()
    main(config)