import re

def is_valid_email(email:str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def collect_input(subject: str, recipient: str, message: str, sender: str):
    if not subject or not recipient or not message or not sender:
        return None, "All fields are required."
    
    if not is_valid_email(recipient):
        return None, "Invalid recipient email address."
    
    return (subject, recipient, message, sender), None