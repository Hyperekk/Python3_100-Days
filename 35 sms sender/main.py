import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


ACC_SID = "AC71c79fae4e1af80a8293e9c359a2354f"
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

API_KEY = os.environ.get("OWM_API_KEY")
LAT = 27.9477595
LONG = -82.458444
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
PARAMETERS = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "minutely,daily,current",
    "appid": API_KEY
}

response = requests.get(ENDPOINT,params=PARAMETERS)
response.raise_for_status()

data = response.json()
codes=[]

will_rain = False
for i in range(13):
    code = data["hourly"][i]["weather"][0]["id"]
    if code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(ACC_SID, AUTH_TOKEN,http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today.",
        from_='+12135284585',
        to='+48609059009'
    )
    print(message.status)


