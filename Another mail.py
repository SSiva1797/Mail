import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# environment variables
username = '<email>'
password = '<password>'

msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" # .format(name="Justin", website='cfe.sh')


def format_msg(my_name, my_website):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg


email_body = format_msg(my_name="Siva S", my_website="www.ss.com")


def send_mail(text=email_body, subject='Hello World', from_email='Varun S <varuns17997@gmail.com>', to_emails=None,
              html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html is not None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()


send_mail(to_emails=['varuns17997@gmail.com'])
