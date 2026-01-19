# 07_iot_sensor.py
import time
import random
import pandas as pd

rows = []
for i in range(10):
    temp = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 70), 2)
    rows.append({"reading": i+1, "temp": temp, "humidity": humidity})
    time.sleep(0.1)

df = pd.DataFrame(rows)
print(df)
df.to_csv("sensor_data.csv", index=False)
print("\nSaved to sensor_data.csv")
