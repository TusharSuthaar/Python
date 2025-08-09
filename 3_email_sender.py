#!/usr/bin/env python3
"""
Email Sender - Send emails using SMTP
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def send_email():
    """Send an email using Gmail SMTP"""
    print("=== Email Sender ===")
    
    sender_email = input("Enter your email address: ")
    sender_password = getpass.getpass("Enter your app password (hidden): ")
    receiver_email = input("Enter receiver's email address: ")
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
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    send_email() 