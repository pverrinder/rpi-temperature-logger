
import numpy as np
import bme280
import smbus2
from time import sleep
import time

port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(humidity, pressure, ambient_temperature)
    sleep(1)


"""
# Define the duration in seconds
duration = 10

# Initialize an empty list to store timestamps
timestamps = []

# Record timestamps every second for the specified duration
for _ in range(duration):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    timestamps.append(current_time)
    time.sleep(1)

# Write the list of timestamps to a file
with open('timestamps.txt', 'w') as file:
    for timestamp in timestamps:
        file.write(f'{timestamp}\n')

print(f'Timestamps recorded and saved to timestamps.txt')
"""
