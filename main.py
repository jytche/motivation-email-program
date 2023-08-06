import smtplib
import datetime as dt
import random

# GENERATE LIST OF QUOTES
with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines()

# CHECK IF TODAY IS THE DAY TO SEND AN EMAIL
now = dt.datetime.now()
current_weekday = now.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_name = days[current_weekday]


def send_motivation():
    global weekday_name
    global quotes_list
    my_email = "#ENTER EMAIL HERE"
    password = "#ENTER PASSWORD HERE"

    with smtplib.SMTP("ENTER EMAIL SMTP DETAILS HERE") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ENTER RECIPIENT ADDRESS", msg=f"Subject:{weekday_name} "
                                                                                       f"Motivation\n\n"
                                                                                       f"{random.choice(quotes_list)}")


if current_weekday == 0:
    send_motivation()