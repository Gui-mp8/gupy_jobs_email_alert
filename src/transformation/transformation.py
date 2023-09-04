from datetime import datetime
from datetime import date
from typing import Dict,List,Any
import time

from utils.logger import log

class Transform():
    def __init__(self, json_data: Dict[str, Any]) -> None:
        self.json_data = json_data

    def change_type(self) -> List[Dict[str,Any]]:
        data_list = [
            {
                'company_name': data['company_name'],
                'job_name': data['job_name'],
                'job_location': data['job_location'],
                'job_type': data['job_type'],
                'job_date_creation': datetime.strptime(data['job_date_creation'].replace('/', '-'), '%d-%m-%Y').date().strftime('%Y-%m-%d') if data['job_date_creation'] else None,
                'job_link': data['job_link']
            }
            for data in self.json_data
        ]
        log().info('Data Treated part 1')
        return data_list

    def data_filter(self) -> List[Dict[str, Any]]:
        today = date.today().strftime('%Y-%m-%d')
        filtered_data = list(
            filter(
                lambda data: data['job_date_creation'] == today,
                self.change_type()
            )
        )
        log().info(f'Data Treated part 2')

        if not filtered_data:
            log().info("There is no job data today")

        log().info(filtered_data)
        return filtered_data

    def etl_result(self) -> List[Dict[str,Any]]:
        return self.data_filter()
