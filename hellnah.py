from env import env
import requests
import network
from lcd import Lcd_i2c
from machine import I2C, Pin
import utime
import time

from test1 import test1
from test2 import test2

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(env["wifi_ssid"])
timeout = 10
while timeout > 0 and wlan.status() < 3:
    print("Connecting to Wi-Fi...")
    time.sleep(1)
    timeout -= 1

if wlan.status() != 3:
    print("Wi-Fi connection failed.")
    exit()
else:
    print("Connected to Wi-Fi! hihihihihi")
    print("IP:", wlan.ifconfig()[0])
    
print(test1["lat"], test1["lon"])

print()
    
# http://ip-api.com/json   
print(f'https://api.openweathermap.org/data/2.5/weather?lat={test1["lat"]}&lon={test1["lon"]}&appid={env["api_key"]}')

start = utime.time()
end = 0
while True:
    if end - start > 2:
        print("ahh")
        start = utime.time()
    end = utime.time()
    

 

