#!/usr/bin/env python3
"""
Anonymous Email Sender - Send emails using SendGrid API
"""

import sendgrid
from sendgrid.helpers.mail import Mail
import getpass

def send_anonymous_email():
    """Send an anonymous email using SendGrid"""
    print("=== Anonymous Email Sender (SendGrid) ===")
    print("Note: You need a SendGrid API key to use this service.")
    print("Get one from: https://sendgrid.com/")
    
    api_key = getpass.getpass("Enter your SendGrid API Key (hidden): ")
    from_email = input("Enter sender email address: ")
    to_email = input("Enter recipient email address: ")
    subject = input("Enter email subject: ")
    
    print("Enter email body (press Enter twice to finish):")
    body_lines = []
    while True:
        line = input()
        if line == "":
            break
        body_lines.append(line)
    body = "\n".join(body_lines)
    
    try:
        sg = sendgrid.SendGridAPIClient(api_key)
        email = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            plain_text_content=body
        )
        
        response = sg.send(email)
        print("✅ Anonymous email sent successfully!")
        print(f"Status Code: {response.status_code}")
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    send_anonymous_email() 