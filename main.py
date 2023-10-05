import schedule
import time
import requests

def get_data(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,relativehumidity_2m,precipitation_probability,windspeed_10m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1"
    response = requests.get(url)
    data = response.json()
    return data;

def send_update():
    #Hardcoded latitude and longitude for Cstat
    lat = 30.6280
    long = 96.3344
    
    data = get_data(lat, long)

def main():
    schedule.every().day().at("06:00").do(send_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()