import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PRICE_APIKEY = os.environ.get("STOCK_PRICE_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = os.environ.get("NEWS_API_KEY")
account_sid = "ACf3bfbb6f2c8b1af9c0eaee94f76d86a2"
auth_token = os.environ.get("AUTH_TOKEN")
sender_number = os.environ.get("SENDER_NUMBER")
recipient_number = os.environ.get("RECIPIENT_NUMBER")

parameters ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "datatype": "json",
    "apikey": STOCK_PRICE_APIKEY
}

response = requests.get(url=STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for key, value in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_data = data_list[1]
day_before_closing_price = float(day_before_data["4. close"])

difference = abs(yesterday_closing_price - day_before_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

percentage_difference = round((difference / yesterday_closing_price) * 100)

if abs(percentage_difference) > 5:
    news_parameters = {
        "apiKey": NEWS_APIKEY,
        "q": COMPANY_NAME,
        "language": "en",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    articles_formatted = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline:{article['title']}.\nBrief:{article['description']}" for article in three_articles]
    for element in articles_formatted:
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=element, from_=sender_number, to=recipient_number)
        print(message.sid)
