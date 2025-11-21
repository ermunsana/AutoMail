import smtplib
import time
from email.message import EmailMessage
from datetime import datetime
import os

SENDER = ""
APP_PASSWORD = ""
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
LOG_FILE = "log.txt"


recipients = [
    ""
]

SUBJECT = ""
BODY = """

"""

ATTACHMENT = "mac.pdf" 


def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def send_emails():
    try:
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login(SENDER, APP_PASSWORD)
        log("Login successful.")
    except Exception as e:
        log(f"Login failed: {e}")
        return

    for recipent in recipients:
        msg = EmailMessage()
        msg["From"] = SENDER
        msg["To"] = recipent
        msg["Subject"] = SUBJECT
        msg.set_content(BODY)

        if os.path.exists(ATTACHMENT):
            with open(ATTACHMENT, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(ATTACHMENT)
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
        else:
            log(f"Attachment not found: {ATTACHMENT}")

        try:
            smtp.send_message(msg)
            log(f"Email sent to {recipent}")
        except Exception as e:
            log(f"Failed to send to {recipent}: {e}")

        time.sleep(.5)
    smtp.quit()
    log("All done.")

if __name__ == "__main__":
    send_emails()