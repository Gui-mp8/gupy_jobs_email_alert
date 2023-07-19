from bs4 import BeautifulSoup
import requests
import re
import json

class WebScraper():
    def __init__(self,config) -> None:
        self.url = 'https://portal.gupy.io/job-search/term=' + config['research']

    def soup(self):
        response = requests.get(url=self.url)
        return BeautifulSoup(response.content, 'html.parser')
    
    def extract_data_to_json(self):
        job_blocks = self.soup().find_all('div',class_="sc-jqUVSM gjodCt sc-70b75bd4-2 kwKQYT")
        data_list = [
            {
                'company_name': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-5 dCVCel').get_text(),
                'job_name': job_block.find('h4', class_='sc-llJcti bGqDEZ sc-70b75bd4-7 ftHylk').get_text(),
                'job_location': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-4 sc-70b75bd4-6 cpauqG jJvUPa').get_text(),
                'job_type': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-4 cpauqG').get_text(),
                'job_date_creation': job_block.find(text=re.compile(r'\d{2}/\d{2}/\d{4}'))
            }
            for job_block in job_blocks
        ]

        return data_list

# config = load_config()
# url = f"https://portal.gupy.io/job-search/term={config['research']}"

# response = requests.get(url=url)
# soup = BeautifulSoup(response.content, 'html.parser')
# job_blocks = soup.find_all('div',class_="sc-jqUVSM gjodCt sc-70b75bd4-2 kwKQYT")

# data_list = [
#     {
#         'company_name': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-5 dCVCel').get_text(),
#         'job_name': job_block.find('h4', class_='sc-llJcti bGqDEZ sc-70b75bd4-7 ftHylk').get_text(),
#         'job_location': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-4 sc-70b75bd4-6 cpauqG jJvUPa').get_text(),
#         'job_type': job_block.find('p', class_='sc-efBctP dpAAMR sc-70b75bd4-4 cpauqG').get_text(),
#         'job_date_creation': job_block.find(text=re.compile(r'\d{2}/\d{2}/\d{4}'))
#     }
#     for job_block in job_blocks
# ]

# print(json.dumps(data_list))