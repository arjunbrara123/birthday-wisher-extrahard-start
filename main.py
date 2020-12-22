##################### Extra Hard Starting Project ######################

import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv

with open("birthdays.csv") as file:
    data = pandas.read_csv(file)

# 2. Check if today matches a birthday in the birthdays.csv

this_month = dt.datetime.now().month
this_day = dt.datetime.now().day

my_email = input("What is your hotmail email? ")
pwd = input(f"Email: {my_email}, Password: ")

for row in data.itertuples():
    if this_month == int(row.month) and this_day == int(row.day):
        name = row.name
        email = row.email

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open("letter_templates\letter_" + str(random.randint(1, 3)) + ".txt") as file:
            letter = file.read().replace("[NAME]", name)
        msg = "Subject:Happy Birthday!\n\n"+letter
# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.live.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=pwd)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=msg)


