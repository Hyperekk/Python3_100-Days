from twilio.rest import Client
ACC_SID = "AC71c79fae4e1af80a8293e9c359a2354f"
AUTH_TOKEN = "9be53882761fb440fbda1bf5591c1ebd"

client = Client(account_sid, auth_token) 

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )