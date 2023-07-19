from bs4 import BeautifulSoup
import requests
import re
import json

response = requests.get(url='https://portal.gupy.io/job-search/term=dados')
soup = BeautifulSoup(response.content, 'html.parser')
job_blocks = soup.find_all('div',class_="sc-jqUVSM gjodCt sc-70b75bd4-2 kwKQYT")

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

print(json.dumps(data_list))