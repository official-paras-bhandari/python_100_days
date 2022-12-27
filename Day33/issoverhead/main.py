import requests
from datetime import datetime
import time

MY_LAT = 28.394857  # Your latitude
MY_LONG = 84.124008  # Your longitude


# If the ISS is close to my current position
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = ifloat(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT + -5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# it is currently dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    # Then email me to tell me to look up.
    if is_iss_overhead() and is_night():
        my_email = "testingpurpose994@gmail.com"
        password = "testingpurpose994@123"
        with smtplib.SMTP("stmp.google.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="bhandariparash75@gmail.com",
                                msg=f"Subject:look Up\n\n ISS is above you in the sky.")
