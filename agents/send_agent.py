import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request

from email.mime.base import MIMEBase
from email import encoders

# If modifying these SCOPES, delete the token.json file
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def authenticate_gmail_api():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)


def send_email(recipient, subject, message, sender, attachments=None):
    try:
        service = authenticate_gmail_api()

        mime_message = MIMEMultipart()
        mime_message["to"] = recipient
        mime_message["from"] = sender
        mime_message["subject"] = subject
        mime_message.attach(MIMEText(message, "plain"))

        # Attach files if any
        if attachments:
            for file in attachments:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition", f'attachment; filename="{file.name}"'
                )
                mime_message.attach(part)

        raw_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
        message = {"raw": raw_message}

        send_message = (
            service.users().messages().send(userId="me", body=message).execute()
        )
        return True, f"Email sent successfully! Message ID: {send_message['id']}"

    except Exception as e:
        return False, f"Failed to send email: {e}"
