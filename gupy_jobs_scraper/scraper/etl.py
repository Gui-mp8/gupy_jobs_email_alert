from scraper.web_scraper import WebScraper

from datetime import datetime
from datetime import date
import json

class Etl(WebScraper):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.json_data = WebScraper(config).extract_data_to_json()

    def change_type(self):
        data_list = [
            {
                'company_name': data['company_name'],
                'job_name': data['job_name'],
                'job_location': data['job_location'],
                'job_type': data['job_type'],
                'job_date_creation': datetime.strptime(data['job_date_creation'].replace('/', '-'), '%d-%m-%Y').date().strftime('%Y-%m-%d')
            }
            for data in self.json_data
        ]

        return data_list
    
    def data_filter(self):
        today = date.today().strftime('%Y-%m-%d')
        filtered_data = [
            data 
            for data in self.change_type()
            if data['job_date_creation'] == today
        ]

        return filtered_data
    
    def etl_result(self):
        return self.data_filter()