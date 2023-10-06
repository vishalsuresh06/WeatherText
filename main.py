import schedule
import time
import requests
import TwilioInfo
from twilio.rest import Client

def get_data(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1"
    response = requests.get(url)
    data = response.json()
    return data

def c_to_F(cel):
    return (cel * (9.0/5) + 32)

def send_update():
    #Hardcoded latitude and longitude for Cstat
    lat = 30.6280
    long = 96.3344
    
    data = get_data(lat, long)
    temp = data["hourly"]["temperature_2m"][0]
    humidity = data["hourly"]["relativehumidity_2m"][0]
    wind = data["hourly"]["windspeed_10m"][0]
    rain = data["hourly"]["precipitation"][0]
    
    info = (
        f"Good morning!\nCurrent weather in College Station:\nTemperature: {c_to_F(temp):.2f}°F\nRelative Humidity: {humidity}%\nWind Speed: {wind} mph\nPrecipitation: {rain} in\n"
    )
    
    send_text(info)
    
def send_text(body):
    client = Client(TwilioInfo.SID, TwilioInfo.Token)
    
    message = client.messages.create(
        body=body,
        from_=TwilioInfo.from_Num,
        to=TwilioInfo.to_Num
    )
    print("Message Sent!")
    

def main():
    #schedule.every().day().at("06:00").do(send_update)
    send_update()
    while True:
        schedule.run_pending()
        time.sleep(1)
        return 0
        
if __name__ == "__main__":
    main()