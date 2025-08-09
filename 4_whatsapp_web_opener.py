#!/usr/bin/env python3
"""
WhatsApp Web Opener - Open WhatsApp Web with pre-filled message
"""

import webbrowser
import urllib.parse

def open_whatsapp_web():
    """Open WhatsApp Web with a pre-filled message"""
    print("=== WhatsApp Web Opener ===")
    
    phone_number = input("Enter phone number (with country code, e.g., +91xxxxxxxxxx): ")
    message = input("Enter your message: ")
    
    # Remove + from phone number if present
    phone_number = phone_number.replace("+", "")
    
    # URL encode the message
    encoded_message = urllib.parse.quote(message)
    
    # Create WhatsApp URL
    url = f"https://wa.me/{phone_number}?text={encoded_message}"
    
    try:
        webbrowser.open(url)
        print("✅ WhatsApp Web opened successfully!")
        print("Note: You can now send the message directly from WhatsApp Web.")
    except Exception as e:
        print(f"❌ Error opening WhatsApp Web: {e}")

if __name__ == "__main__":
    open_whatsapp_web() 