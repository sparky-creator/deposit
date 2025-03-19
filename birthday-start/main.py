##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "sternparky@gmail.com"
password = "bcsl szdo mrzg ydkj"

# with open("birthdays.csv") as bday_info:
#     lines = bday_info.readlines()

lines_in_pd = pd.read_csv("birthdays.csv")

print(lines_in_pd)

month = dt.datetime.now().month
date = dt.datetime.now().day

month_index = lines_in_pd.loc[lines_in_pd.month == month].index.tolist()
date_index = lines_in_pd.loc[lines_in_pd.day == date].index.tolist()

common_index = [index for index in date_index if index in month_index]

#----- Choosing Random Letter

list_letters = ["letter_1.txt","letter_2.txt","letter_2.txt" ]

for index in range(len(common_index)):
    with open(f"letter_templates/{random.choice(list_letters)}") as letter:
        line = letter.read()
        new_name = lines_in_pd.name.iloc[common_index[index]]
        new_line = line.replace("[NAME]", new_name )
        print(new_line)

#---- sending emails

    #smtp object
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Happy_Birthday!\n\n {new_line}"
        )




