
import numpy as np
import csv
import bme280
import smbus2
import time

"""
# Sensor Setup
port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)
"""



# Measurement interval (seconds)
measurement_interval = 1

# Total run time (seconds). This is the length of a single data file
total_time = 10

# Number of repetitions. i.e. the number of times to repeat total_time
rep = 2


# CSV file header
csv_header = ['Date', 'Time', 'Temperature (C)', 'Humidity (%)', 'Pressure (mb)']


for i in range(rep):
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    csv_filename = 'data_' + timestamp + '.csv'  # Name of the CSV file

    with open(csv_filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(csv_header)

    count = measurement_interval
    while count <= total_time:
        humidity = 75.4
        temperature = 20.3
        pressure = 1000
        
        current_date = time.strftime("%Y%m%d", time.localtime())
        current_time = time.strftime("%H%M%S", time.localtime())
        
        data_row = [current_date, current_time, f'{temperature:.2f}', f'{humidity:.2f}', f'{pressure:.2f}']
        
        
        with open(csv_filename, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow(data_row)
          
        #print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} % - Recorded at {current_time}")
    
        time.sleep(measurement_interval)
        count = count + measurement_interval



"""
while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(humidity, pressure, ambient_temperature)
    sleep(1)
"""






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
