##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
current_time = dt.datetime.now()
today_tuple = (current_time.month, current_time.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as file:
        content = file.read()
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        content = content.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.

    my_email = "sgwgw91@gmail.com"
    password = "(abc12345)"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="heilysuan@yahoo.com",
                            msg=f"Subject: Happy Birthday \n\n {content}")
