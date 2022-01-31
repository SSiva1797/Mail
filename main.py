import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

USERNAME = os.environ.get("MAIL_USER")
PASSWORD = os.environ.get("MAIL_PASS")

message = MIMEMultipart()
message["From"] = f"Varun S <{USERNAME}>"
message["To"] = USERNAME
message["Subject"] = "Reg- Information about our client"
body = ("Dear User\n\nPlease find the attachment with your requested data about our client.\nThe attach "
        "file is password protected and the default password for the same is in the form of "
        "'user@ddmmyyyy'\n where user is username in lowercase and ddmmyyyy is Date of Birth(in ddmmyyyy "
        "Format)")

message.attach(MIMEText(_text=body, _subtype='plain'))

# open the file to be sent
filename = "Lorem ipsum.pdf"
attachment = open(file="C:\\Users\\siva1\\PycharmProjects\\Mail\\Lorem ipsum.pdf", mode="rb")

# instance of MIMEBase and named as p
p = MIMEBase(_maintype="application", _subtype="octet-stream")

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header(_name="Content-Disposition", _value="attachment; filename= %s" % filename)

# attach the instance 'p' to 'message'
message.attach(payload=p)

# create SMTP_SSL session
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp_server:
    smtp_server.login(user=USERNAME, password=PASSWORD)
    text = message.as_string()
    smtp_server.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg=text)
