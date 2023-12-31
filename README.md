# Gupy job alert

This project has the goal to send an email alert from the desired jobs that you want.

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
- It's necessary to download [Docker](https://docs.docker.com/engine/install/ubuntu/) and create an account at [Docker Hub](https://hub.docker.com).

- It's necessary to have a Google email and [configure it](https://support.google.com/accounts/answer/185833?hl=en) to receive the email.

- Creates a copy of `sample_config.json` and rename it to `config.json`.

- Creates a copy of `.env.eample` and rename it to `.env`

## Configurations

1 - Change the config.json key values to your respective data.

- **research** = It's the keyword that acess your desired jobs
- **days_before_today** = It represents the number you want to subtract from today to see the jobs on that day.
- **user_email** =  Is the email of Who'll send the email.
- **password** = Your Google App password, that it's generated after the guide at the **Prerequisites**.
- **receiver_email** = the email or email's that'll receive the message.

2 - Add data to .env based on your credentials

- **DOCKER_USERNAME**: It's your Docker Hub login
- **DOCKER_PASSWORD**: It's your Docker Hub password

## Running the Program

After setting config.json and .env, just run the code below

```
make run
```
