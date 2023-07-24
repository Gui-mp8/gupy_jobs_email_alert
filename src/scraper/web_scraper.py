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

            job_blocks = soup.find_all('div', class_="sc-70b75bd4-0 hojCpd")
            data_list = [
                {
                    'company_name': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-5 dCVCel').get_text(),
                    'job_name': job_block.find('h4', class_='sc-llJcti bGqDEZ sc-70b75bd4-7 ftHylk').get_text(),
                    'job_location': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-4 sc-70b75bd4-6 cpauqG jJvUPa').get_text(),
                    'job_type': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-4 cpauqG').get_text(),
                    'job_date_creation': job_block.find(text=re.compile(r'\d{2}/\d{2}/\d{4}')),
                    'job_link': job_block.find('a')['href']
                }
                for job_block in job_blocks
            ]

            self.data.extend(data_list)
        return self.data

