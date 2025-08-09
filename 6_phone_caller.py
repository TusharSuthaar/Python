#!/usr/bin/env python3
"""
Phone Caller - Make phone calls using Twilio API
"""

from twilio.rest import Client
import getpass

def make_phone_call():
    """Make a phone call using Twilio"""
    print("=== Phone Caller (Twilio) ===")
    print("Note: You need a Twilio account and phone number to use this service.")
    
    account_sid = input("Enter your Twilio Account SID: ")
    auth_token = getpass.getpass("Enter your Twilio Auth Token (hidden): ")
    from_number = input("Enter your Twilio phone number (e.g., +1234567890): ")
    to_number = input("Enter recipient's phone number (e.g., +1234567890): ")
    
    print("\nChoose message type:")
    print("1. Default message ('Hello from Python!')")
    print("2. Custom message")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "2":
        custom_message = input("Enter your custom message: ")
        twiml_message = f"<Response><Say>{custom_message}</Say></Response>"
    else:
        twiml_message = "<Response><Say>Hello from Python!</Say></Response>"
    
    try:
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            twiml=twiml_message,
            from_=from_number,
            to=to_number
        )
        print(f"✅ Call initiated successfully!")
        print(f"Call SID: {call.sid}")
    except Exception as e:
        print(f"❌ Error making call: {e}")

if __name__ == "__main__":
    make_phone_call() 