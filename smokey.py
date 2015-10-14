__author__ = 'Dan'
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText


amt_per_day = 15.0
interval_days = 180
awake_time = 15.0
quit_interval = 259200
current_interval = 60*60*(awake_time/amt_per_day)
interval_dif = quit_interval - current_interval

wake = 8
sleep = 1

interval_per_day = interval_dif/interval_days
interval_per_hour = interval_per_day/24

last_cigarrette = 0
last_update = 0

app_email = "smokeytheapp@gmail.com"
password = "****"
phone_email = "****@txt.att.net"

message = MIMEText("This is your alert from Smokey! Enjoy your cigarette!")
message['Subject'] = "Smokey Alert!"
message['From'] = app_email
message['To'] = phone_email


def send_email():
    s = smtplib.SMTP('smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login(app_email, password)
    s.sendmail(app_email, [phone_email], message.as_string())
    s.quit()


def determine_next_email(last_update, last_cigarrette, current_interval):
    sending = True
    while True:
        if time.time() - last_update >= 3600:
            last_update = time.time()
            current_interval += interval_per_hour
        if time.time() - last_cigarrette >= current_interval:
            print current_interval
            if sending:
                send_email()
            last_cigarrette = time.time()
        if datetime.now().hour < wake and datetime.now().hour > sleep:
            sending = False
        else:
            sending = True

if __name__ == "__main__":
    determine_next_email(0,0,current_interval)