# Python Automation Programs

This repository contains 12 separate Python automation programs extracted from the main Streamlit app. Each program can be run independently to perform specific automation tasks.

## ✅ Prefer the Streamlit Dashboard

You can run all of these programs inline from the dashboard with inputs and outputs rendered in the browser.

- Start the dashboard:
  ```powershell
  .\automation_env\Scripts\Activate.ps1; streamlit run automation_app.py
  ```
- Use the top navigation to choose a Category and Program
- Read usage, fill inputs, and see results inline

Or, run any script directly as described below.

## 📋 Programs List

1. **`1_ram_monitor.py`** - Monitor system RAM usage
2. **`2_whatsapp_sender.py`** - Send scheduled WhatsApp messages
3. **`3_email_sender.py`** - Send emails via SMTP
4. **`4_whatsapp_web_opener.py`** - Open WhatsApp Web with pre-filled messages
5. **`5_sms_sender.py`** - Send SMS using Twilio
6. **`6_phone_caller.py`** - Make phone calls using Twilio
7. **`7_google_search.py`** - Perform Google searches
8. **`8_twitter_poster.py`** - Post tweets to Twitter/X
9. **`9_website_downloader.py`** - Download and parse website content
10. **`10_anonymous_email.py`** - Send emails using SendGrid
11. **`11_tuple_vs_list.py`** - Compare tuples vs lists with examples
12. **`12_image_creator.py`** - Create digital images

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Any Program

```bash
python 1_ram_monitor.py
```

## 📖 Program Details

### 1. RAM Monitor (`1_ram_monitor.py`)
- **Purpose**: Check system memory usage
- **Dependencies**: `psutil`
- **Usage**: Simply run the program to see current RAM statistics
- **Output**: Total, available, used memory in GB and percentage

### 2. WhatsApp Sender (`2_whatsapp_sender.py`)
- **Purpose**: Schedule WhatsApp messages
- **Dependencies**: `pywhatkit`
- **Requirements**: None (uses WhatsApp Web)
- **Usage**: Enter phone number, message, and time to send
- **Note**: WhatsApp Web will open automatically at scheduled time

### 3. Email Sender (`3_email_sender.py`)
- **Purpose**: Send emails via Gmail SMTP
- **Dependencies**: `smtplib` (built-in)
- **Requirements**: Gmail account with App Password
- **Setup**: Enable 2FA and generate App Password in Gmail settings
- **Usage**: Enter sender/receiver emails, subject, and body

### 4. WhatsApp Web Opener (`4_whatsapp_web_opener.py`)
- **Purpose**: Open WhatsApp Web with pre-filled message
- **Dependencies**: `webbrowser` (built-in)
- **Requirements**: None
- **Usage**: Enter phone number and message
- **Note**: Opens browser with WhatsApp Web ready to send

### 5. SMS Sender (`5_sms_sender.py`)
- **Purpose**: Send SMS messages
- **Dependencies**: `twilio`
- **Requirements**: Twilio account and phone number
- **Setup**: Get Account SID and Auth Token from Twilio Console
- **Usage**: Enter Twilio credentials, phone numbers, and message

### 6. Phone Caller (`6_phone_caller.py`)
- **Purpose**: Make automated phone calls
- **Dependencies**: `twilio`
- **Requirements**: Twilio account and phone number
- **Features**: Default or custom voice messages
- **Usage**: Enter Twilio credentials, phone numbers, and message

### 7. Google Search (`7_google_search.py`)
- **Purpose**: Perform Google searches programmatically
- **Dependencies**: `googlesearch-python`
- **Requirements**: None
- **Usage**: Enter search query and number of results
- **Output**: List of URLs matching the search

### 8. Twitter Poster (`8_twitter_poster.py`)
- **Purpose**: Post tweets to Twitter/X
- **Dependencies**: `tweepy`
- **Requirements**: Twitter Developer Account
- **Setup**: Get API keys from Twitter Developer Portal
- **Usage**: Enter API credentials and tweet text
- **Note**: Automatically truncates tweets longer than 280 characters

### 9. Website Downloader (`9_website_downloader.py`)
- **Purpose**: Download and parse website content
- **Dependencies**: `requests`, `beautifulsoup4`
- **Requirements**: None
- **Features**: Download HTML, parse content, save to file
- **Usage**: Enter website URL, optionally save content

### 10. Anonymous Email (`10_anonymous_email.py`)
- **Purpose**: Send emails via SendGrid API
- **Dependencies**: `sendgrid`
- **Requirements**: SendGrid account and API key
- **Setup**: Get API key from SendGrid dashboard
- **Usage**: Enter API key, sender/receiver emails, subject, and body

### 11. Tuple vs List (`11_tuple_vs_list.py`)
- **Purpose**: Educational comparison of tuples and lists
- **Dependencies**: `sys`, `time` (built-in)
- **Requirements**: None
- **Features**: Performance comparison, memory usage, practical examples
- **Usage**: Run to see comprehensive comparison

### 12. Image Creator (`12_image_creator.py`)
- **Purpose**: Create digital images with custom properties
- **Dependencies**: `Pillow`
- **Requirements**: None
- **Features**: Custom dimensions, colors, text overlay
- **Usage**: Enter image specifications and optional text

## 🔧 Setup Requirements

### API Keys and Accounts Needed:

1. **Gmail** (for email sender):
   - Enable 2-Factor Authentication
   - Generate App Password: Google Account → Security → App passwords

2. **Twilio** (for SMS and calls):
   - Sign up at [twilio.com](https://twilio.com)
   - Get Account SID and Auth Token from Console
   - Purchase a phone number

3. **Twitter/X** (for posting):
   - Apply for Developer Account at [developer.twitter.com](https://developer.twitter.com)
   - Create an app and get API keys

4. **SendGrid** (for anonymous email):
   - Sign up at [sendgrid.com](https://sendgrid.com)
   - Generate API key from Settings → API Keys

## 🛡️ Security Notes

- Never commit API keys or passwords to version control
- Use environment variables for sensitive data
- App passwords are safer than regular passwords for email
- Keep Twilio and SendGrid API keys secure

## ⚠️ Important Notes

- Some programs require internet connection
- WhatsApp programs work only if WhatsApp Web is accessible
- Rate limits may apply to API-based services
- Some services may have costs (Twilio, SendGrid)

## 🐛 Troubleshooting

### Common Issues:

1. **Import Errors**: Install missing packages with `pip install package-name`
2. **WhatsApp Not Opening**: Check if WhatsApp Web is accessible in your browser
3. **Email Authentication Failed**: Ensure App Password is correct and 2FA is enabled
4. **Twilio Errors**: Verify Account SID, Auth Token, and phone number format
5. **Twitter API Errors**: Check if API keys are valid and have proper permissions

### Getting Help:

- Check error messages for specific issues
- Verify all required credentials are correct
- Ensure internet connection is stable
- Review API documentation for external services

## 📝 License

These programs are provided as-is for educational and automation purposes. Please respect the terms of service of all external APIs and services used. 