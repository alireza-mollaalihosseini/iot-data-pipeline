def is_anomaly(data):
    if data["temperature"] > 75 or data["co2"] > 1000:
        return True
    return False
