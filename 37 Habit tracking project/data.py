from datetime import date, datetime

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

USERNAME = "hyperekk"
TOKEN = "MK20041020"
GRAPH_ID = "graph1"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

params_2nd = {
    "id": GRAPH_ID,
    "name": "Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

params_3rd = {
    "date": "20220112",
    "quantity": "2",
}

params_4th = {
    "quantity": "4",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
