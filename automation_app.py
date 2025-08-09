#!/usr/bin/env python3
"""
Python Automation Toolkit Launcher
Runs individual automation programs
"""

import streamlit as st
import subprocess
import sys
import os

# --------------------------------------
# Streamlit App Title
# --------------------------------------
st.title("📌 Python Automation Toolkit")
st.write("Choose a task to run the corresponding automation program!")

# Check if all program files exist
program_files = {
    "Read RAM": "1_ram_monitor.py",
    "Send WhatsApp Message": "2_whatsapp_sender.py", 
    "Send Email": "3_email_sender.py",
    "Send WhatsApp Without Saving Contact": "4_whatsapp_web_opener.py",
    "Send SMS": "5_sms_sender.py",
    "Make a Phone Call": "6_phone_caller.py",
    "Google Search": "7_google_search.py",
    "Post on Twitter (X)": "8_twitter_poster.py",
    "Download Website Data": "9_website_downloader.py",
    "Send Anonymous Email": "10_anonymous_email.py",
    "Tuple vs List Difference": "11_tuple_vs_list.py",
    "Create Digital Image": "12_image_creator.py",
}

# --------------------------------------
# Menu
# --------------------------------------
task = st.selectbox("Choose a task", list(program_files.keys()))

# --------------------------------------
# Program Launcher
# --------------------------------------

if st.button(f"Run {task}", type="primary"):
    program_file = program_files[task]
    
    if not os.path.exists(program_file):
        st.error(f"❌ Program file '{program_file}' not found!")
        st.write("Make sure all program files are in the same directory.")
    else:
        st.info(f"🚀 Launching {program_file}...")
        st.write("**Note:** The program will run in your terminal/command prompt.")
        st.write("Check your terminal window to interact with the program.")
        
        try:
            # Run the program in a new terminal/command prompt
            if sys.platform.startswith('win'):
                # Windows
                subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', f'python {program_file}'])
            elif sys.platform.startswith('darwin'):
                # macOS
                subprocess.Popen(['osascript', '-e', f'tell app "Terminal" to do script "python {program_file}"'])
            else:
                # Linux
                subprocess.Popen(['gnome-terminal', '--', 'python3', program_file])
            
            st.success(f"✅ {task} program launched successfully!")
            st.write("The program is now running in a separate terminal window.")
            
        except Exception as e:
            st.error(f"❌ Error launching program: {e}")
            st.write("**Fallback:** You can run the program manually:")
            st.code(f"python {program_file}", language="bash")

# --------------------------------------
# Information Section
# --------------------------------------

st.markdown("---")
st.subheader("📋 Available Programs")

col1, col2 = st.columns(2)

with col1:
    st.write("**System & Communication:**")
    st.write("• RAM Monitor")
    st.write("• Email Sender") 
    st.write("• SMS Sender")
    st.write("• Phone Caller")
    st.write("• Anonymous Email")
    
with col2:
    st.write("**Web & Social:**")
    st.write("• WhatsApp Sender")
    st.write("• WhatsApp Web Opener")
    st.write("• Google Search")
    st.write("• Twitter Poster")
    st.write("• Website Downloader")

st.write("**Utilities:**")
st.write("• Tuple vs List Comparison")
st.write("• Digital Image Creator")

# --------------------------------------
# Setup Information
# --------------------------------------

st.markdown("---")
st.subheader("🔧 Setup Requirements")

with st.expander("View Setup Instructions"):
    st.write("**Dependencies Installation:**")
    st.code("pip install -r requirements.txt", language="bash")
    
    st.write("**API Keys Needed for Some Programs:**")
    st.write("• **Gmail**: App Password (for email sender)")
    st.write("• **Twilio**: Account SID + Auth Token (for SMS/calls)")
    st.write("• **Twitter**: API Keys (for posting)")
    st.write("• **SendGrid**: API Key (for anonymous email)")
    
    st.write("**Manual Program Execution:**")
    st.write("You can also run any program directly from terminal:")
    st.code("python 1_ram_monitor.py", language="bash")

# --------------------------------------
# File Status Check
# --------------------------------------

st.markdown("---")
st.subheader("📁 Program Files Status")

missing_files = []
existing_files = []

for task_name, filename in program_files.items():
    if os.path.exists(filename):
        existing_files.append(filename)
    else:
        missing_files.append(filename)

if existing_files:
    st.success(f"✅ {len(existing_files)} program files found")
    with st.expander("View existing files"):
        for file in existing_files:
            st.write(f"• {file}")

if missing_files:
    st.error(f"❌ {len(missing_files)} program files missing")
    with st.expander("View missing files"):
        for file in missing_files:
            st.write(f"• {file}")
        st.write("**Note:** Make sure all program files are in the same directory as this launcher.")

# --------------------------------------
# Footer
# --------------------------------------

st.markdown("---")
st.write("**Note:** This launcher opens programs in separate terminal windows for better interaction.")
st.write("For detailed documentation, check `PROGRAMS_README.md`")
