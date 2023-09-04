from bs4 import BeautifulSoup
import requests
from typing import Dict, List, Any
from utils.logger import log
from lxml import etree

class WebScraper:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.base_url = 'https://portal.gupy.io/job-search/term='
        self.config = config
        self.data = []

    def extract_data_to_json(self) -> List[Dict[str, Any]]:
        log().info("Starting scraping...")
        for research in self.config['research']:
            url = self.base_url + research
            response = requests.get(url=url)
            soup = BeautifulSoup(response.content, 'html.parser')
            soup_x = etree.HTML(str(soup))
            html_blocks = soup.find_all('div', class_='sc-a3bd7ea-0 HCzvP')

            data_list = []
            li = 0
            for html_block in html_blocks:
                li+=1
                company_name_data = soup_x.xpath(f'//*[@id="__next"]/div[3]/div/div/main/ul/li[{li}]/div/a/div/div[1]/p')
                job_name_data = soup_x.xpath(f'//*[@id="__next"]/div[3]/div/div/main/ul/li[{li}]/div/a/div/h2')
                job_location_data = soup_x.xpath(f'//*[@id="__next"]/div[3]/div/div/main/ul/li[{li}]/div/a/div/div[2]/div[1]/span')
                job_type_data = soup_x.xpath(f'//*[@id="__next"]/div[3]/div/div/main/ul/li[{li}]/div/a/div/div[2]/div[2]/span')
                job_date_creation_data = soup_x.xpath(f'//*[@id="__next"]/div[3]/div/div/main/ul/li[{li}]/div/a/div/div[3]/p')
                job_link = html_block.find('a')['href']

                data_list.append(
                    {
                        'company_name': company_name_data[0].text if company_name_data else None,
                        'job_name': job_name_data[0].text if job_name_data else None,
                        'job_location': job_location_data[0].text if job_location_data else None,
                        'job_type': job_type_data[0].text if job_type_data else None,
                        'job_date_creation': job_date_creation_data[0].text.split(': ')[1] if job_date_creation_data else None,
                        'job_link': job_link if job_link else None
                    }
                )

            self.data.extend(data_list)
            # log().info(self.data)

        if not self.data:
            log().warning("Probably the page structure has changed.")

        return self.data
