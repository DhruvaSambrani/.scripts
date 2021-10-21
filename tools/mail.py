#!/usr/bin/env python3

import smtplib as slib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import random
import os.path
import json

me = json.load(open("creds.json", "r"))

to = input("To: ").split(", ")
subject = str(input("Subject: "))
attachments = []
while True:
    if t := input("Attachment path: "):
        attachments.append(t)
    else:
        break

body = str(input("Body: "))

print()

msg = MIMEMultipart()
msg['From'] = me["email"]
msg['To'] = ", ".join(to)
msg['Subject'] = subject
msg.attach(MIMEText(body, "html"))
for i in attachments:
    with open(i, "rb") as file:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((file).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',
                     f"attachment; filename= {os.path.basename(i)}")
        msg.attach(p)


try:
    server = slib.SMTP_SSL("smtp.gmail.com")
    server.ehlo()
    server.login(me["email"], me["pswd"])
    server.sendmail(me["email"], to, msg.as_string())
    server.close()

except Exception as e:
    print("Failed with error:")
    print(e)
