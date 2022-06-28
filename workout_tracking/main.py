import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('bgdanterty', 'bod3563993')
APP_ID = "d886bc67"
API_KEY = "24ba72b52907282d762cf752c0d9124d"

GENDER = "male"
WEIGHT_KG = 98
HEIGHT_CM = 187
AGE = 25

exersice_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("What did you do?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exersice_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety_endpoint = "https://api.sheety.co/2126ff04ad89ea8ebb5025b7b7e7441d/myWorkouts/workouts"

for exercise in result["exercises"]:
    inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(sheety_endpoint, json=inputs, auth=basic)
    print(response.text)
