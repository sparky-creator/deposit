import smtplib
import datetime as dt
import random

#---Getting Random Quotes

now = dt.datetime.now()
day_index = now.weekday()

with open("quotes.txt") as quote:
    lines = quote.readlines()

email_line = random.choice(lines)


#---- EMAILING Session
my_email = "sternparky@gmail.com"
password = "bcsl szdo mrzg ydkj"

#smtp object
with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Motivation Quote\n\n {email_line}"
    )


