import requests
from twilio.rest import Client
from config import *

parameters = {
    "lat": 42.020859,
    "lon": 23.094337,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=api_url, params=parameters)
response.raise_for_status()
data = response.json()
weather_codes = [hour_data["weather"][0]["id"] for hour_data in data["list"]]

will_rain = False
for code in weather_codes:
    if int(code) < 700:
       will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = (client.messages
               .create(
        body="It's going to rain today. Remember to bring bring un umbrella",
        from_=from_number,
        to=to_number))
    print(message.status)