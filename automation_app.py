#!/usr/bin/env python3
"""
Python Automation Toolkit Dashboard
Comprehensive Streamlit dashboard for managing automation programs
"""

import streamlit as st
import subprocess
import sys
import os
import json
import time
from datetime import datetime
import psutil

# --------------------------------------
# Page Configuration
# --------------------------------------
st.set_page_config(
    page_title="Python Automation Toolkit",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------
# Custom CSS
# --------------------------------------
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .program-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #007bff;
        margin: 0.5rem 0;
    }
    .status-running {
        background-color: #d4edda;
        color: #155724;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
    }
    .status-stopped {
        background-color: #f8d7da;
        color: #721c24;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------
# Initialize Session State
# --------------------------------------
if 'execution_log' not in st.session_state:
    st.session_state.execution_log = []

if 'program_status' not in st.session_state:
    st.session_state.program_status = {}

# --------------------------------------
# Program Configuration
# --------------------------------------
PROGRAM_CONFIG = {
    "system": {
        "title": "🖥️ System Tools",
        "programs": {
            "Read RAM": {
                "file": "1_ram_monitor.py",
                "description": "Monitor system memory usage",
                "category": "System",
                "dependencies": ["psutil"],
                "requires_input": False
            }
        }
    },
    "communication": {
        "title": "📱 Communication",
        "programs": {
            "Send WhatsApp Message": {
                "file": "2_whatsapp_sender.py",
                "description": "Send scheduled WhatsApp messages",
                "category": "Communication",
                "dependencies": ["pywhatkit"],
                "requires_input": True
            },
            "Send Email": {
                "file": "3_email_sender.py",
                "description": "Send emails via Gmail SMTP",
                "category": "Communication", 
                "dependencies": ["smtplib"],
                "requires_input": True
            },
            "Send WhatsApp Without Saving Contact": {
                "file": "4_whatsapp_web_opener.py",
                "description": "Open WhatsApp Web with pre-filled message",
                "category": "Communication",
                "dependencies": ["webbrowser"],
                "requires_input": True
            },
            "Send SMS": {
                "file": "5_sms_sender.py",
                "description": "Send SMS using Twilio API",
                "category": "Communication",
                "dependencies": ["twilio"],
                "requires_input": True
            },
            "Make a Phone Call": {
                "file": "6_phone_caller.py",
                "description": "Make automated phone calls",
                "category": "Communication",
                "dependencies": ["twilio"],
                "requires_input": True
            },
            "Send Anonymous Email": {
                "file": "10_anonymous_email.py",
                "description": "Send emails using SendGrid API",
                "category": "Communication",
                "dependencies": ["sendgrid"],
                "requires_input": True
            }
        }
    },
    "web": {
        "title": "🌐 Web & Social",
        "programs": {
            "Google Search": {
                "file": "7_google_search.py",
                "description": "Perform Google searches",
                "category": "Web",
                "dependencies": ["googlesearch-python"],
                "requires_input": True
            },
            "Post on Twitter (X)": {
                "file": "8_twitter_poster.py",
                "description": "Post tweets to Twitter/X",
                "category": "Social",
                "dependencies": ["tweepy"],
                "requires_input": True
            },
            "Download Website Data": {
                "file": "9_website_downloader.py",
                "description": "Download and parse website content",
                "category": "Web",
                "dependencies": ["requests", "beautifulsoup4"],
                "requires_input": True
            }
        }
    },
    "utilities": {
        "title": "🛠️ Utilities",
        "programs": {
            "Tuple vs List Difference": {
                "file": "11_tuple_vs_list.py",
                "description": "Educational comparison of tuples vs lists",
                "category": "Educational",
                "dependencies": [],
                "requires_input": False
            },
            "Create Digital Image": {
                "file": "12_image_creator.py",
                "description": "Create custom digital images",
                "category": "Creative",
                "dependencies": ["Pillow"],
                "requires_input": True
            }
        }
    }
}

# --------------------------------------
# Helper Functions
# --------------------------------------

def log_execution(program_name, status, message=""):
    """Log program execution"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "program": program_name,
        "status": status,
        "message": message
    }
    st.session_state.execution_log.insert(0, log_entry)
    # Keep only last 50 entries
    st.session_state.execution_log = st.session_state.execution_log[:50]

def get_system_info():
    """Get system information"""
    try:
        mem = psutil.virtual_memory()
        cpu_percent = psutil.cpu_percent(interval=1)
        return {
            "ram_total": mem.total / (1024**3),
            "ram_used": mem.used / (1024**3),
            "ram_percent": mem.percent,
            "cpu_percent": cpu_percent
        }
    except Exception:
        return None

def check_file_exists(filename):
    """Check if program file exists"""
    return os.path.exists(filename)

def run_program(program_file, program_name):
    """Run a program and handle the execution"""
    if not check_file_exists(program_file):
        log_execution(program_name, "ERROR", f"File {program_file} not found")
        return False
    
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
        
        log_execution(program_name, "LAUNCHED", f"Program launched in new terminal")
        return True
        
    except Exception as e:
        log_execution(program_name, "ERROR", str(e))
        return False

# --------------------------------------
# Main Dashboard
# --------------------------------------

# Header
st.markdown("""
<div class="main-header">
    <h1>🚀 Python Automation Toolkit Dashboard</h1>
    <p>Comprehensive automation suite with 12 powerful tools</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🎛️ Control Panel")
    
    # System Information
    st.subheader("📊 System Status")
    sys_info = get_system_info()
    if sys_info:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("RAM Usage", f"{sys_info['ram_percent']:.1f}%", 
                     f"{sys_info['ram_used']:.1f}GB / {sys_info['ram_total']:.1f}GB")
        with col2:
            st.metric("CPU Usage", f"{sys_info['cpu_percent']:.1f}%")
    
    # Quick Actions
    st.subheader("⚡ Quick Actions")
    if st.button("🔄 Refresh Dashboard", use_container_width=True):
        st.rerun()
    
    if st.button("🧹 Clear Logs", use_container_width=True):
        st.session_state.execution_log = []
        st.success("Logs cleared!")
    
    # File Status
    st.subheader("📁 File Status")
    total_files = 0
    missing_files = 0
    
    for category in PROGRAM_CONFIG.values():
        for program_name, config in category["programs"].items():
            total_files += 1
            if not check_file_exists(config["file"]):
                missing_files += 1
    
    if missing_files == 0:
        st.success(f"✅ All {total_files} programs found")
    else:
        st.error(f"❌ {missing_files} of {total_files} programs missing")

# Main Content Area
"""
Inline Program Runner UI with top navigation and inline inputs/outputs
"""

# Top navigation bar
nav_col1, nav_col2, nav_col3 = st.columns([1.2, 1.6, 1.2])

# Map visible category titles to keys
title_to_key = {cfg["title"]: key for key, cfg in PROGRAM_CONFIG.items()}
with nav_col1:
    selected_title = st.selectbox("Category", list(title_to_key.keys()))
category_key = title_to_key[selected_title]

with nav_col2:
    program_names = list(PROGRAM_CONFIG[category_key]["programs"].keys())
    selected_program = st.selectbox("Program", program_names)

with nav_col3:
    sys_info = get_system_info()
    if sys_info:
        st.metric("CPU", f"{sys_info['cpu_percent']:.0f}%")
        st.metric("RAM", f"{sys_info['ram_percent']:.0f}%")

# Usage details
cfg = PROGRAM_CONFIG[category_key]["programs"][selected_program]
st.markdown(
    f"""
<div class=\"program-card\">
  <h3>📘 Usage: {selected_program}</h3>
  <p>{cfg['description']}</p>
  <p class=\"tiny\"><strong>Dependencies:</strong> {', '.join(cfg['dependencies']) if cfg['dependencies'] else 'None'}</p>
</div>
""",
    unsafe_allow_html=True,
)

# Inline implementations for each program
def render_read_ram():
    import psutil as _ps
    mem = _ps.virtual_memory()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total (GB)", f"{mem.total / (1024**3):.2f}")
    c2.metric("Used (GB)", f"{mem.used / (1024**3):.2f}")
    c3.metric("Available (GB)", f"{mem.available / (1024**3):.2f}")
    c4.metric("Percent", f"{mem.percent:.1f}%")
    log_execution("Read RAM", "LAUNCHED", "Displayed RAM stats")


def render_whatsapp_sender():
    st.info("Requires WhatsApp Web.")
    mode = st.radio("Mode", ["Send instantly", "Schedule"], horizontal=True)
    phone = st.text_input("Phone number (with country code)", placeholder="+91xxxxxxxxxx")
    message = st.text_area("Message")
    if mode == "Schedule":
        a, b = st.columns(2)
        with a:
            hour = st.number_input("Hour (24h)", 0, 23, 12)
        with b:
            minute = st.number_input("Minute", 0, 59, 0)
    else:
        hour = minute = None
    if st.button("Send via WhatsApp"):
        try:
            import pywhatkit as pwk
            if mode == "Send instantly":
                pwk.sendwhatmsg_instantly(phone, message, wait_time=15, tab_close=True)
            else:
                pwk.sendwhatmsg(phone, message, int(hour), int(minute))
            st.success("Triggered in WhatsApp Web.")
            log_execution("Send WhatsApp Message", "LAUNCHED", mode)
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Send WhatsApp Message", "ERROR", str(e))


def render_email_sender():
    st.warning("Use Gmail App Password (2FA).")
    sender = st.text_input("Sender email")
    app_password = st.text_input("App password", type="password")
    receiver = st.text_input("Receiver email")
    subject = st.text_input("Subject")
    body = st.text_area("Body")
    if st.button("Send Email"):
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            msg = MIMEMultipart()
            msg["From"] = sender
            msg["To"] = receiver
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, app_password)
                server.sendmail(sender, receiver, msg.as_string())
            st.success("Email sent.")
            log_execution("Send Email", "LAUNCHED", f"To: {receiver}")
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Send Email", "ERROR", str(e))


def render_whatsapp_web_opener():
    phone = st.text_input("Phone number (with country code)")
    message = st.text_input("Prefilled message")
    if st.button("Generate Chat Link"):
        try:
            import urllib.parse
            url = f"https://wa.me/{phone.replace('+','')}?text={urllib.parse.quote(message)}"
            st.link_button("Open chat", url)
            log_execution("WhatsApp Web Opener", "LAUNCHED", url)
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("WhatsApp Web Opener", "ERROR", str(e))


def render_sms_sender():
    st.info("Twilio credentials required.")
    sid = st.text_input("Twilio Account SID")
    token = st.text_input("Twilio Auth Token", type="password")
    from_num = st.text_input("From (Twilio number)", "+1234567890")
    to_num = st.text_input("To (recipient)", "+1234567890")
    text = st.text_area("Message")
    if st.button("Send SMS"):
        try:
            from twilio.rest import Client
            client = Client(sid, token)
            msg = client.messages.create(body=text, from_=from_num, to=to_num)
            st.success(f"Sent SID: {msg.sid}")
            log_execution("Send SMS", "LAUNCHED", f"To: {to_num}")
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Send SMS", "ERROR", str(e))


def render_phone_caller():
    st.info("Twilio credentials required.")
    sid = st.text_input("Twilio Account SID")
    token = st.text_input("Twilio Auth Token", type="password")
    from_num = st.text_input("From (Twilio number)", "+1234567890")
    to_num = st.text_input("To (recipient)", "+1234567890")
    mode = st.radio("Message", ["Default: 'Hello from Python!'", "Custom"], horizontal=True)
    custom = st.text_input("Custom text") if mode == "Custom" else ""
    if st.button("Make Call"):
        try:
            from twilio.rest import Client
            twiml = f"<Response><Say>{custom or 'Hello from Python!'}</Say></Response>"
            client = Client(sid, token)
            call = client.calls.create(twiml=twiml, from_=from_num, to=to_num)
            st.success(f"Call SID: {call.sid}")
            log_execution("Phone Call", "LAUNCHED", f"To: {to_num}")
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Phone Call", "ERROR", str(e))


def render_google_search():
    query = st.text_input("Search query")
    num = st.number_input("Number of results", 1, 20, 5)
    if st.button("Search"):
        try:
            from googlesearch import search
            results = list(search(query, num_results=int(num)))
            if results:
                for i, url in enumerate(results, 1):
                    st.write(f"{i}. ", url)
            else:
                st.info("No results found.")
            log_execution("Google Search", "LAUNCHED", query)
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Google Search", "ERROR", str(e))


def render_twitter_poster():
    st.info("Twitter/X developer credentials required.")
    api_key = st.text_input("API Key")
    api_secret = st.text_input("API Secret", type="password")
    access_token = st.text_input("Access Token")
    access_secret = st.text_input("Access Token Secret", type="password")
    tweet = st.text_area("Tweet (max 280 chars)")
    if st.button("Post Tweet"):
        try:
            import tweepy
            auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
            api = tweepy.API(auth)
            api.verify_credentials()
            if len(tweet) > 280:
                tweet = tweet[:280]
            api.update_status(tweet)
            st.success("Tweet posted.")
            log_execution("Twitter Post", "LAUNCHED", tweet[:50])
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Twitter Post", "ERROR", str(e))


def render_website_downloader():
    url = st.text_input("URL", "https://example.com")
    if st.button("Fetch"):
        try:
            import requests
            from bs4 import BeautifulSoup
            _url = url if url.startswith(("http://", "https://")) else "https://" + url
            resp = requests.get(_url, timeout=15)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.title.string if soup.title else "(no title)"
            st.success(f"Fetched. Status {resp.status_code}. Title: {title}")
            html = soup.prettify()
            st.text_area("HTML (first 3000 chars)", html[:3000], height=300)
            st.download_button("Download HTML", data=html, file_name="website_data.html")
            log_execution("Website Downloader", "LAUNCHED", _url)
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Website Downloader", "ERROR", str(e))


def render_anonymous_email():
    st.info("SendGrid API key required.")
    api_key = st.text_input("SendGrid API Key", type="password")
    from_email = st.text_input("From email")
    to_email = st.text_input("To email")
    subject = st.text_input("Subject")
    body = st.text_area("Body")
    if st.button("Send via SendGrid"):
        try:
            import sendgrid
            from sendgrid.helpers.mail import Mail
            sg = sendgrid.SendGridAPIClient(api_key)
            email = Mail(from_email=from_email, to_emails=to_email, subject=subject, plain_text_content=body)
            resp = sg.send(email)
            st.success(f"Sent. Status: {resp.status_code}")
            log_execution("Anonymous Email", "LAUNCHED", f"To: {to_email}")
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Anonymous Email", "ERROR", str(e))


def render_tuple_vs_list():
    import sys as _sys
    import time as _time
    tup = (1, 2, 3, 4, 5)
    lst = [1, 2, 3, 4, 5]
    c1, c2 = st.columns(2)
    with c1:
        st.write("Tuple:", tup)
    with c2:
        st.write("List:", lst)
    c3, c4 = st.columns(2)
    c3.metric("Tuple bytes", _sys.getsizeof(tup))
    c4.metric("List bytes", _sys.getsizeof(lst))
    t0 = _time.time()
    for _ in range(100000):
        _ = (1, 2, 3, 4, 5)
    t_tuple = _time.time() - t0
    t0 = _time.time()
    for _ in range(100000):
        _ = [1, 2, 3, 4, 5]
    t_list = _time.time() - t0
    st.write(f"Creation time — tuple: {t_tuple:.4f}s, list: {t_list:.4f}s")
    log_execution("Tuple vs List", "LAUNCHED", "Compared tuple vs list")


def render_image_creator():
    from io import BytesIO
    from PIL import Image, ImageDraw, ImageFont
    a, b = st.columns(2)
    with a:
        width = st.number_input("Width", 50, 4000, 400)
        height = st.number_input("Height", 50, 4000, 300)
        bg = st.color_picker("Background color", "#FFFFFF")
    with b:
        add_text = st.checkbox("Add centered text")
        text = st.text_input("Text", value="") if add_text else ""
        font_size = st.number_input("Font size", 8, 200, 24) if add_text else 24
        text_color = st.color_picker("Text color", "#000000") if add_text else "#000000"
    if st.button("Create Image"):
        try:
            img = Image.new("RGB", (int(width), int(height)), bg)
            if add_text and text:
                draw = ImageDraw.Draw(img)
                try:
                    font = ImageFont.truetype("arial.ttf", int(font_size))
                except Exception:
                    font = ImageFont.load_default()
                bbox = draw.textbbox((0, 0), text, font=font)
                tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
                x, y = (int(width) - tw) // 2, (int(height) - th) // 2
                draw.text((x, y), text, fill=text_color, font=font)
            buf = BytesIO()
            img.save(buf, format="PNG")
            st.image(img, caption=f"{int(width)}x{int(height)}", use_column_width=True)
            st.download_button("Download PNG", data=buf.getvalue(), file_name="my_image.png", mime="image/png")
            log_execution("Image Creator", "LAUNCHED", f"{width}x{height}")
        except Exception as e:
            st.error(f"Error: {e}")
            log_execution("Image Creator", "ERROR", str(e))

# Router
if selected_program == "Read RAM":
    render_read_ram()
elif selected_program == "Send WhatsApp Message":
    render_whatsapp_sender()
elif selected_program == "Send Email":
    render_email_sender()
elif selected_program == "Send WhatsApp Without Saving Contact":
    render_whatsapp_web_opener()
elif selected_program == "Send SMS":
    render_sms_sender()
elif selected_program == "Make a Phone Call":
    render_phone_caller()
elif selected_program == "Google Search":
    render_google_search()
elif selected_program == "Post on Twitter (X)":
    render_twitter_poster()
elif selected_program == "Download Website Data":
    render_website_downloader()
elif selected_program == "Send Anonymous Email":
    render_anonymous_email()
elif selected_program == "Tuple vs List Difference":
    render_tuple_vs_list()
elif selected_program == "Create Digital Image":
    render_image_creator()

# Logs (compact)
st.markdown("---")
st.subheader("📝 Execution Log")
if st.session_state.execution_log:
    for log in st.session_state.execution_log[:25]:
        st.write(f"[{log['timestamp']}] {log['program']} — {log['status']} — {log['message']}")
else:
    st.info("No actions yet.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🚀 Python Automation Toolkit Dashboard | Built with Streamlit</p>
    <p>For detailed documentation, check <code>PROGRAMS_README.md</code></p>
</div>
""", unsafe_allow_html=True)
