import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

AV_API_KEY = str(os.environ.get("AV_API_KEY"))
NEWS_API_KEY = str(os.environ.get("NEWS_API_KEY"))
TWILIO_AUTH = "KEY"
TWILIO_SID = "KEY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": AV_API_KEY
}
parameters_news = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,

}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

request = requests.get(STOCK_ENDPOINT,parameters)
data = request.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yst_close = round(float(yesterday_data['4. close']),2)
print(yst_close)

day_b4 = round(float(data_list[1]['4. close']),2)
print(day_b4)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = round(yst_close - day_b4,2)
print(difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = round(abs((difference) / yst_close) * 100,2)
print(percent_diff)

if percent_diff > 5:
    pull = requests.get(NEWS_ENDPOINT,parameters_news)
    news = pull.json()
    articles = news["articles"][0]

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_article = [f"Headline: {articles['title']}. \nBrief: {articles['description']}"]
#TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(TWILIO_SID,TWILIO_AUTH)
    message = client.messages \
            .create(
                body=formatted_article,
                from_='NUMBER',
                to='NUMBER'
            )



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

