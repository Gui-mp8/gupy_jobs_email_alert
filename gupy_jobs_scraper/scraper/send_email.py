from utils.config import load_config

import smtplib
import ssl
from email.message import EmailMessage
from datetime import date
from typing import Dict, List, Any


class SendEmail():
    def __init__(self, config: Dict[str, Any]) -> None:
        self.user_email = config["user_email"]
        self.password = config["password"]
        self.receiver_email = config["receiver_email"]
        self.message = EmailMessage()

    def create_email(self, json_data: List[Dict[str, Any]]) -> EmailMessage:
        today = date.today().strftime('%Y-%m-%d')

        self.message['From'] = self.user_email
        self.message['To'] = self.receiver_email
        self.message['Subject'] = f'Gupy Vagas {today}'

        # Create a HTML table to display the job data
        body = f'''
            <h2>Vagas de hoje:</h2>
            <table border="1">
                <tr>
                    <th>Empresa</th>
                    <th>Cargo</th>
                    <th>Tipo</th>
                    <th>Localidade</th>
                </tr>
        '''

        # Iterate over the list of JSON data and add each job's data as a row in the table
        for data in json_data:
            body += f'''
                <tr>
                    <td>{data['company_name']}</td>
                    <td>{data['job_name']}</td>
                    <td>{data['job_type']}</td>
                    <td>{data['job_location']}</td>
                </tr>
            '''

        body += '</table>'

        # Set the content type to 'text/html' to use HTML formatting in the email body
        self.message.add_alternative(body, subtype='html')

        context = ssl.create_default_context()
        return context

    def send_email(self, json_data: List[Dict[str, Any]]):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.create_email(json_data)) as smtp:
            smtp.login(self.user_email, self.password)
            smtp.sendmail(self.user_email, self.receiver_email, self.message.as_string())

        return print("Email sent successfully!")
