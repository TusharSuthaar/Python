import streamlit as st
import psutil
import pywhatkit
import smtplib
import webbrowser
from twilio.rest import Client
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
import sendgrid
from sendgrid.helpers.mail import Mail

# --------------------------------------
# Streamlit App Title
# --------------------------------------
st.title("📌 Python Automation Toolkit")
st.write("Perform multiple automation tasks from one place!")

# --------------------------------------
# Menu
# --------------------------------------
task = st.selectbox("Choose a task", [
    "Read RAM",
    "Send WhatsApp Message",
    "Send Email",
    "Send WhatsApp Without Saving Contact",
    "Send SMS",
    "Make a Phone Call",
    "Google Search",
    "Post on Twitter (X)",
    "Download Website Data",
    "Send Anonymous Email",
    "Tuple vs List Difference",
    "Create Digital Image",
])

# --------------------------------------
# Task Implementations
# --------------------------------------

# 1. Read RAM
if task == "Read RAM":
    mem = psutil.virtual_memory()
    st.write(f"**Total:** {mem.total / (1024**3):.2f} GB")
    st.write(f"**Available:** {mem.available / (1024**3):.2f} GB")
    st.write(f"**Used:** {mem.used / (1024**3):.2f} GB")
    st.write(f"**Percentage:** {mem.percent}%")

# 2. Send WhatsApp Message
elif task == "Send WhatsApp Message":
    number = st.text_input("Enter Phone Number (+91...)")
    message = st.text_area("Enter Message")
    hour = st.number_input("Hour (24hr format)", 0, 23, 12)
    minute = st.number_input("Minute", 0, 59, 0)
    if st.button("Send Message"):
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        st.success("Message Scheduled!")

# 3. Send Email
elif task == "Send Email":
    sender = st.text_input("Sender Email")
    password = st.text_input("Sender App Password", type="password")
    receiver = st.text_input("Receiver Email")
    subject = st.text_input("Subject")
    body = st.text_area("Body")
    if st.button("Send Email"):
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, f"Subject: {subject}\n\n{body}")
        st.success("Email Sent!")

# 4. Send WhatsApp Without Saving Contact
elif task == "Send WhatsApp Without Saving Contact":
    phone_number = st.text_input("Enter Phone Number (+91...)")
    message = st.text_area("Enter Message")
    if st.button("Open WhatsApp Web"):
        webbrowser.open(f"https://wa.me/{phone_number}?text={message}")
        st.success("WhatsApp Web Opened!")

# 5. Send SMS
elif task == "Send SMS":
    sid = st.text_input("Twilio SID")
    token = st.text_input("Twilio Auth Token", type="password")
    from_num = st.text_input("Twilio Number")
    to_num = st.text_input("Receiver Number")
    sms_body = st.text_area("Message")
    if st.button("Send SMS"):
        client = Client(sid, token)
        message = client.messages.create(body=sms_body, from_=from_num, to=to_num)
        st.success(f"SMS Sent! SID: {message.sid}")

# 6. Make a Phone Call
elif task == "Make a Phone Call":
    sid = st.text_input("Twilio SID")
    token = st.text_input("Twilio Auth Token", type="password")
    from_num = st.text_input("Twilio Number")
    to_num = st.text_input("Receiver Number")
    if st.button("Call Now"):
        client = Client(sid, token)
        call = client.calls.create(
            twiml="<Response><Say>Hello from Python!</Say></Response>",
            from_=from_num,
            to=to_num
        )
        st.success(f"Call Initiated! SID: {call.sid}")

# 7. Google Search
elif task == "Google Search":
    query = st.text_input("Enter Search Query")
    if st.button("Search"):
        results = list(search(query, num_results=5))
        for r in results:
            st.write(r)

# 8. Post on Twitter (X)
elif task == "Post on Twitter (X)":
    import tweepy
    api_key = st.text_input("API Key")
    api_secret = st.text_input("API Secret")
    access_token = st.text_input("Access Token")
    access_secret = st.text_input("Access Secret")
    tweet = st.text_area("Tweet Text")
    if st.button("Post Tweet"):
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
        api = tweepy.API(auth)
        api.update_status(tweet)
        st.success("Tweet Posted!")

# 9. Download Website Data
elif task == "Download Website Data":
    url = st.text_input("Enter Website URL")
    if st.button("Download"):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        st.code(soup.prettify()[:3000])  # Limit display

# 10. Send Anonymous Email
elif task == "Send Anonymous Email":
    api_key = st.text_input("SendGrid API Key")
    from_email = st.text_input("From Email")
    to_email = st.text_input("To Email")
    subject = st.text_input("Subject")
    body = st.text_area("Body")
    if st.button("Send Anon Email"):
        sg = sendgrid.SendGridAPIClient(api_key)
        email = Mail(from_email=from_email, to_emails=to_email, subject=subject, plain_text_content=body)
        sg.send(email)
        st.success("Anonymous Email Sent!")

# 11. Tuple vs List Difference
elif task == "Tuple vs List Difference":
    st.table({
        "Feature": ["Mutability", "Syntax", "Performance", "Use Case", "Memory Usage"],
        "Tuple": ["Immutable", "()", "Faster", "Fixed Data", "Less"],
        "List": ["Mutable", "[]", "Slower", "Dynamic Data", "More"]
    })

# 12. Create Digital Image
elif task == "Create Digital Image":
    width = st.number_input("Width", 100, 1000, 200)
    height = st.number_input("Height", 100, 1000, 200)
    color = st.color_picker("Choose Color", "#FFFFFF")
    if st.button("Create Image"):
        img = Image.new("RGB", (width, height), color)
        img.save("my_image.png")
        st.image(img)
        st.success("Image Created!")
