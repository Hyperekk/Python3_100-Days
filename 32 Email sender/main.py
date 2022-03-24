import datetime as dt
import pandas as pd
import random
import smtplib

MAIL = "TO FILL - UR ACC"
PASSWORD = "TO FILL - UR ACC"

##################### Normal Starting Project ######################

data = pd.read_csv("birthdays.csv")

today = dt.datetime.now()
today = (today.month,today.day)

new_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today in new_dict:
    name = new_dict[today]["name"]
    person_mail = new_dict[today]["email"]
    rand = random.randint(1,3)
    with open(f"letter_templates/letter_{rand}.txt","r") as f:
        letter = f.read()
        letter = letter.replace("[NAME]",name)
    
    message = f"From:Maciej\nSubject:Happy Birthday!\n\n{letter}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MAIL,password=PASSWORD)
        connection.sendmail(from_addr=MAIL,to_addrs=person_mail,msg=message)




