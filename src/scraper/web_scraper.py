from bs4 import BeautifulSoup
import requests
import re
from typing import Dict, List, Any
import logging

class WebScraper:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.base_url = 'https://portal.gupy.io/job-search/term='
        self.config = config
        self.data = []

    def extract_data_to_json(self) -> List[Dict[str, Any]]:
        for research in self.config['research']:
            url = self.base_url + research
            response = requests.get(url=url)
            soup = BeautifulSoup(response.content, 'html.parser')

            job_blocks = soup.find_all('div', class_="sc-f31b108-0 bChLuL")
            data_list = [
                {
                    'company_name': job_block.find('p', class_='sc-efBctP dpAAMR sc-f31b108-6 jguNee').get_text(),
                    'job_name': job_block.find('h2', class_='sc-llJcti jgKUZ sc-f31b108-5 dILyqK').get_text(),
                    'job_location': job_block.find('span', class_='sc-23336bc7-1 cezNaf').get_text(),
                    'job_type': [job_type.get_text() for job_type in job_block.find_all('span', class_='sc-23336bc7-1 cezNaf')[1:]],
                    'job_date_creation': job_block.find('p', class_='sc-efBctP dpAAMR sc-1db88588-0 inqtnx').get_text().split(': ')[1],
                    'job_link': job_block.find('a')['href']
                }
                for job_block in job_blocks
            ]

            self.data.extend(data_list)
        return self.data
