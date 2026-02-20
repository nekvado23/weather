from env import env
import requests
import network
from lcd import Lcd_i2c
from machine import I2C, Pin
import utime

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
display = Lcd_i2c(i2c)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(env["wifi_ssid"])
timeout = 10
while timeout > 0 and wlan.status() < 3:
    print("Connecting to Wi-Fi...")
    utime.sleep(1)
    timeout -= 1

if wlan.status() != 3:
    print("Wi-Fi connection failed.")
    exit()
else:
    print("Connected to Wi-Fi! hihihihihi")
    print("IP:", wlan.ifconfig()[0])

def get_data():
    try:
        url = "http://ip-api.com/json"
        data = requests.get(url)
        if(data.status_code == 200):
            raw=data.json()
            lat = raw["lat"]
            lon = raw["lon"]
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={env["api_key"]}'
        data = requests.get(url)
        if(data.status_code == 200):
            raw=data.json()
            display.set_cursor(0,0)
            display.write("temp: " + str(raw["main"]["temp"]))
            display.set_cursor(0,1)
            display.write("hum: " + str(raw["main"]["humidity"]))
    except:
        print("error")
            
get_data()
start = utime.time()
end = 0
while True:
    if end - start > 10 * 60:
        get_data()
        start = utime.time()
    end = utime.time()
    

 

