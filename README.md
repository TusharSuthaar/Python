# Python Automation Toolkit

A collection of 12 automation utilities with a Streamlit dashboard that lets you choose a program, read usage, provide inputs, and see outputs inline.

## Features

- Top navigation bar to pick Category and Program
- Usage details and dependencies per program
- Inputs and outputs rendered inline (no external terminal needed)
- Execution log panel
- Works inside a virtual environment

## Programs

- System
  - Read RAM
- Communication
  - Send WhatsApp Message
  - Send Email
  - Send WhatsApp Without Saving Contact
  - Send SMS (Twilio)
  - Make a Phone Call (Twilio)
  - Send Anonymous Email (SendGrid)
- Web & Social
  - Google Search
  - Post on Twitter (X)
  - Download Website Data
- Utilities
  - Tuple vs List Difference
  - Create Digital Image

## Setup

1) Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv automation_env
.\automation_env\Scripts\Activate.ps1
```

2) Install dependencies:

```bash
pip install streamlit -r requirements.txt
```

## Run

```powershell
.\automation_env\Scripts\Activate.ps1; streamlit run automation_app.py
```

- Local URL: http://localhost:8501
- Use the top nav to select a Category and a Program.
- Fill inputs and click the action button to execute. Results show inline.

## Credentials Required (for some tools)

- Gmail: App Password with 2FA (for Send Email)
- Twilio: Account SID, Auth Token, Twilio phone number (for SMS and Calls)
- Twitter/X: API Key, API Secret, Access Token, Access Token Secret (for posting)
- SendGrid: API key (for Anonymous Email)

## Troubleshooting

- If `streamlit` is not found, ensure the virtual environment is activated.
- For WhatsApp actions, your browser must be able to open WhatsApp Web.
- API errors are shown inline with details in the execution log.

## License

This project is provided as-is for educational and automation use. Please follow the terms of service of all third-party APIs.