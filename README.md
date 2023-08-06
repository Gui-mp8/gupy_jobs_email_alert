# Gupy job alert

This project has the goal to send an email alert from the desired jobs that you want.

## Previous Information
It's necessary to install the [chrome-driver](https://chromedriver.chromium.org/downloads). Check your chrome atualization.

## Tecnologies
  <table>
    <tr>
      <td>OS</td>
      <td>Docker</td>
      <td>Python</td>
    </tr>
      <tr>
      <td>Ubuntu</td>
      <td>1 Python container</td>
      <td>3.9</td>
    </tr>
  </table>

## Prerequisites
- It's necessary to download [Docker](https://docs.docker.com/engine/install/ubuntu/).

- It's necessary to have a Google email and [configure it](https://support.google.com/accounts/answer/185833?hl=en) to receive the email.

- Creates a copy of `sample_config.json`, rename it to `config.json`.

## Configurations

It's only necessary to change the config.json key values to your respective data.

- research: It's the keyword that acess your desired jobs
- user_email: Is the email of Who'll send the email.
- password: Your Google App password, that it's generated after the guide at the **Prerequisites**.
- the email that'll receive the message.

## Running the Program

```
docker build -t gupy-jobs-alert .
```
```
docker run gupy-jobs-alert
```