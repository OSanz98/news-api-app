import os
import smtplib
import ssl


def send_email(content):
    host = "smtp.gmail.com"
    port = 465
    username = "impeysanz@gmail.com"
    password = os.getenv("NEWS_API_APP_PASSWORD")

    receiver = "impeysanz@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr=username, to_addrs=receiver, msg=content)
