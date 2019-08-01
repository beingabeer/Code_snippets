import smtplib
import os
import requests

# EMAIL_USER = os.environ.get('EMAIL_USER')
# EMAIL_PASS = os.environ.get('EMAIL_PASS')


r = requests.get('https://www.abeergs.com', timeout=5)

if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_USER, EMAIL_PASS)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(sender, receiver, msg)
