# ===============================
# WhatsApp Automated Message Sender
# ===============================

from twilio.rest import Client
from datetime import datetime, timedelta
import time

# -------------------------------
# Twilio Credentials
# -------------------------------
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


client = Client(account_sid, auth_token)

# -------------------------------
# Send WhatsApp Message Function
# -------------------------------
def send_sms(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",   # Twilio WhatsApp Sandbox
            to=f"whatsapp:{recipient_number}",
            body=message_body
        )
        print(f"✅ Message sent successfully | SID: {message.sid}")
    except Exception as e:
        print("❌ Error sending message:", e)

# -------------------------------
# User Input
# -------------------------------
name = input("Enter Recipient Name: ")
mobile = input("Enter Recipient Mobile Number With Country Code: ")
message_body = input("Enter The Message You Want To Deliver To Recipient: ")

date_str = input("Enter Date To Send The Message {YYYY-MM-DD}: ")
time_str = input("Enter Time To Send The Message {HH:MM}: ")

# -------------------------------
# DateTime Parsing
# -------------------------------
schedule_datetime = datetime.strptime(
    f"{date_str} {time_str}",
    "%Y-%m-%d %H:%M"
)

current_datetime = datetime.now()

# -------------------------------
# Auto-Fix Past Time
# -------------------------------
if schedule_datetime <= current_datetime:
    schedule_datetime = current_datetime + timedelta(minutes=3)
    print("⏰ Entered time was in the past.")
    print("➡ Auto-adjusted to:", schedule_datetime.strftime("%Y-%m-%d %H:%M"))

# -------------------------------
# Calculate Delay
# -------------------------------
delay_seconds = (schedule_datetime - datetime.now()).total_seconds()

print(f"📨 Message scheduled for {name} at {schedule_datetime.strftime('%Y-%m-%d %H:%M')}")

# -------------------------------
# Wait & Send Message
# -------------------------------
time.sleep(delay_seconds)
send_sms(mobile, message_body)