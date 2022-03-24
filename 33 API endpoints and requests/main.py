import requests
import smtplib
import time
from datetime import datetime, timezone

MY_LAT = 52.145620 # Your latitude
MY_LONG = 16.405320 # Your longitude

EMAIL = "EMAIL"
PASSWORD = "PASSWORD"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc).hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

message = '''Subject:LOOK UP!!


LOOK UP NOW!
'''
while True:
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5 and (time_now >= sunset or time_now <= sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL,PASSWORD)
            connection.sendmail(
                from_addr="kurkiewicz.maciej2@gmail.com",
                to_addrs="kurkiewicz.maciej1@gmail.com",
                msg=message,
            )
    time.sleep(60)





