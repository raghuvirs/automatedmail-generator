from agents.input_agent import collect_input
from agents.generation_agent import generate_email
from agents.send_agent import send_email

def run_mail_pipeline(subject, recipient, message, sender, tone, attachments):
    inputs, error = collect_input(subject, recipient, message, sender)
    if error:
        return error
    
    subject, recipient, message, sender = inputs

    generated_message = generate_email(subject, recipient, message, sender, tone)

    success, status_message = send_email(recipient, subject, generated_message, sender, attachments)

    return status_message
