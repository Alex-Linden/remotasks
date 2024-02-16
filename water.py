# # import time
# import requests
# import json

# def check_watering_alerts():
#     # url = "Your data url"
#     # response = requests.get(url).json()
#     response = [{"id":1, "moisture_level":10 }, {"id":15, "moisture_level":10 }, {"id":10, "moisture_level":30 }, {"id":1, "moisture_level":21 }]
#     watering_alerts = ["Sensor " + str(sensor["id"]) + " needs watering." for sensor in response if sensor["moisture_level"] < 20]
#     print("h20", watering_alerts)
#     return watering_alerts

# # # if __name__ == "__main__":
# # #     while True:
# # #         print(check_watering_alerts())
# # #         # You can adjust the sleep time as per your need.
# # #         time.sleep(60)

if __name__ == "__main__":
    print("Hello world!")
    while True:
        print(check_watering_alerts())
        # You can adjust the sleep time as per your need.
        time.sleep(60)

import requests
import time
import json

def check_and_alert(url, threshold):
    while True:
        print("run")
        # response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = {
                "sensor_1": 75,
                "sensor_2": 60,
                "sensor_3": 90
                }

        sensors_to_water = []
        for sensor_id, moisture_level in data.items():
            if moisture_level < threshold:
                sensors_to_water.append(sensor_id)

        if len(sensors_to_water) > 0:
            for sensor_id in sensors_to_water:
                print(f"*****Sensor ID {sensor_id} needs watering*****")
        time.sleep(60) # wait 1 minute before checking again

check_and_alert("https://example.com/sensor-data.json", 70)
