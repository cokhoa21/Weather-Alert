import requests
from twilio.rest import Client

api_key = "69f04e4613056b159c2761a9d9e664d2"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = 'AC5c1e386ac3697ce13ea06af369b9f250'
auth_token = '0498f1195ddb7e7af5e94b7a52bea947'

weather_params = {
    "lat": 21.027763,
    "lon": 105.834160,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

responses = requests.get(OWN_Endpoint, params=weather_params)
responses.raise_for_status()
weather_data = responses.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today.Remember to bring an umbrella.",
        from_='+12705174465',
        to='+84914759722'
    )
    print(message.status)

