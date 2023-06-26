from datetime import datetime
import pandas
import random
import smtplib

email = "pythontesting17@outlook.com"
password = "Kakanati!1"

file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

with open(file_path) as file:
    template = file.read()

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if (today.month, today.day) in new_dict:
    person_name = new_dict[today_tuple]
    new_template = template.replace("[NAME]", person_name["name"])

    with smtplib.SMTP("smtp.office365.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="chanishvili@yahoo.com",
            msg=f"subject:Happy Birthday \n\n{new_template}"
        )
