import smtplib
import ssl
from email.message import EmailMessage
from datetime import date
from typing import Dict, List, Any


class SendEmail():
    def __init__(self, config: Dict[str, Any], json_data: List[Dict[str, Any]]) -> None:
        self.config = config
        self.json_data = json_data
        self.user_email = self.config["user_email"]
        self.password = self.config["password"]
        self.receiver_email = self.config["receiver_email"]
        self.message = EmailMessage()

    def create_email(self) -> EmailMessage:
        today = date.today().strftime('%d-%m-%Y')

        self.message['From'] = self.user_email
        self.message['To'] = self.receiver_email
        self.message['Subject'] = f'Gupy Vagas relacionadas a {self.config["research"]} {today}'

        # Create a HTML table to display the job data
        body = f'''
            <h2>Vagas de hoje:</h2>
            <table border="1">
                <tr>
                    <th>Empresa</th>
                    <th>Cargo</th>
                    <th>Tipo</th>
                    <th>Localidade</th>
                    <th>Link da Vaga</th>
                </tr>
        '''

        # Iterate over the list of JSON data and add each job's data as a row in the table
        for data in self.json_data:
            body += f'''
                <tr>
                    <td>{data['company_name']}</td>
                    <td>{data['job_name']}</td>
                    <td>{data['job_type']}</td>
                    <td>{data['job_location']}</td>
                    <td>{data['job_link']}</td>
                </tr>
            '''

        body += '</table>'

        # Set the content type to 'text/html' to use HTML formatting in the email body
        self.message.add_alternative(body, subtype='html')

        context = ssl.create_default_context()
        return context

    def send_email(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.create_email()) as smtp:
            smtp.login(self.user_email, self.password)
            smtp.sendmail(self.user_email, self.receiver_email, self.message.as_string())

        return print("Email sent successfully!")
