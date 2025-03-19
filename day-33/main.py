import requests
import datetime

response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()

long = float(response_iss.json()["iss_position"]["longitude"])
lat = float(response_iss.json()["iss_position"]["latitude"])

iss_position = (long, lat)
print(iss_position)

LAT =41.533655
LNG = -73.90517

if LAT - 5 < long < LAT +5 and LNG -5 < lat < LNG +5:
    print("NEAR")


parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


print(sunrise)
print(sunset)


time_now = datetime.datetime.now()
print(time_now.hour)