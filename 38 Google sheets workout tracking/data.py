import requests
import datetime
import os

APP_ID = os.environ.get("NUTRITIONIX_ID")
APP_KEY = os.environ.get("NUTRITIONIX_KEY")

current_time = datetime.datetime.now()
time_now = current_time.strftime("%H:%M")
today_date = current_time.strftime("%d/%m/%Y")

auth = os.environ.get('SHEETY_AUTH')
bearer_headers = {"Authorization": f"Bearer {auth}"}

POST_LINK = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_POST = os.environ.get("SHEET_ENDPOINT")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

things = {
 "query": input("What did you do?: "),
 "gender":"male",
 "weight_kg":59,
 "height_cm":174,
 "age":17
}
request = requests.post(url=POST_LINK,json=things,headers=headers)

sheety_data = {
    "workout": {
	    "date": today_date,
	    "time": time_now,
        "exercise": request.json()["exercises"][0]["name"].title(),
        "duration": request.json()["exercises"][0]["duration_min"],
        "calories": request.json()["exercises"][0]["nf_calories"],
    }
}

x = requests.post(SHEETY_POST,json=sheety_data,headers=bearer_headers)
print(x.text)

