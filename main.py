import smtplib
import datetime as dt
import random

with open(file="quotes.txt") as file:
    quotes = file.readlines()

sender = "YOUR MAIL HERE"
password = "YOUR PASSWORD HERE"
receiver = ["RECEIVER MAIL HERE"]
subject = "Motivational quotes!"
text = f"wishes:{random.choice(quotes)}"
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (sender, ", ".join(receiver), subject, text)

date = dt.datetime.now()
day = date.weekday()

if day == 0:
    try:
        with smtplib.SMTP("YOUR MAIL DOMAIN HERE", 587) as connection:
            connection.starttls()
            connection.login(user=sender, password=password)
            connection.sendmail(sender, receiver, message)
            print("Successfully sent email")
            # connection.close() wymagane gdy nie otwieramy przez with
    except smtplib.SMTPException:
        print("Error: unable to send email")

