#!/usr/bin/env python3
"""
SMS Sender - Send SMS using Twilio API
"""

from twilio.rest import Client
import getpass

def send_sms():
    """Send SMS using Twilio"""
    print("=== SMS Sender (Twilio) ===")
    print("Note: You need a Twilio account and phone number to use this service.")
    
    account_sid = input("Enter your Twilio Account SID: ")
    auth_token = getpass.getpass("Enter your Twilio Auth Token (hidden): ")
    from_number = input("Enter your Twilio phone number (e.g., +1234567890): ")
    to_number = input("Enter recipient's phone number (e.g., +1234567890): ")
    message_body = input("Enter your message: ")
    
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )
        print(f"✅ SMS sent successfully!")
        print(f"Message SID: {message.sid}")
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")

if __name__ == "__main__":
    send_sms() 