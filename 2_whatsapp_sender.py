#!/usr/bin/env python3
"""
WhatsApp Message Sender - Send scheduled WhatsApp messages
"""

import pywhatkit

def send_whatsapp_message():
    """Send a WhatsApp message at a specific time"""
    print("=== WhatsApp Message Sender ===")
    
    number = input("Enter phone number (with country code, e.g., +91xxxxxxxxxx): ")
    message = input("Enter your message: ")
    
    print("\nEnter the time to send the message:")
    hour = int(input("Hour (24-hour format, 0-23): "))
    minute = int(input("Minute (0-59): "))
    
    try:
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        print("✅ Message scheduled successfully!")
        print("Note: WhatsApp Web will open automatically at the scheduled time.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    send_whatsapp_message() 