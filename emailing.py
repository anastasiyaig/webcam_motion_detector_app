import os
import smtplib
import imghdr
from email.message import EmailMessage

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
PASSWORD = os.getenv("WEBCAM_APP_GMAIL_PASSWORD")


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
        filename = file.name
        im_type = imghdr.what(None, content)

    email_message.add_attachment(content, maintype="image", subtype=im_type, filename=filename)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER_EMAIL, PASSWORD)
    gmail.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, email_message.as_string())
    gmail.quit()

