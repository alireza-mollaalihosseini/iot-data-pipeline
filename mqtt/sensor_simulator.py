import time
import json
import random
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def generate_data():
    return {
        "device_id": "sensor-001",
        "temperature": random.uniform(20, 100),
        "co2": random.uniform(300, 1200),
        "co": random.uniform(0, 10),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

while True:
    payload = generate_data()
    client.publish("sensors/data", json.dumps(payload))
    print(f"Published: {payload}")
    time.sleep(5)
