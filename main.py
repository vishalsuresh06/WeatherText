import schedule
import time
import requests
import TwilioInfo
from twilio.rest import Client

def get_data(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,relativehumidity_2m,precipitation_probability,windspeed_10m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1"
    response = requests.get(url)
    data = response.json()
    return data

def send_update():
    #Hardcoded latitude and longitude for Cstat
    lat = 30.6280
    long = 96.3344
    
    data = get_data(lat, long)
    temp = ["hourly"]["temperature_2m"][0]
    humidity = ["hourly"]["relativehumidity_2m"][0]
    wind = ["hourly"]["windspeed_10m"][0]
    rain = ["hourly"]["precipitation"][0]
    
    info = (
        f"Good morning!"
        f"Current weather in College Station:\n"
        f"Temperature: {temp:.2f}°F\n"
        f"Relative Humidity: {humidity}%\n"
        f"Wind Speed: {wind} mph\n"
        f"Precipitation: {rain}\n"
    )
    
def send_text(body):
    client = Client(TwilioInfo.SID, TwilioInfo.Token)
    
    message = client.messages.create(
        body=body,
        from_=TwilioInfo.from_Num,
        to=TwilioInfo.to_Num
    )
    print("Message Sent!")
    

def main():
    schedule.every().day().at("06:00").do(send_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()