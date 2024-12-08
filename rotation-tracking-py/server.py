import requests

stream = False

esp32_ip = "192.168.4.1"

integer_value = 0

stream

while True:
    with open('result.txt', 'r') as file:
        integer_value = file.read()
    response = requests.post(f"http://{esp32_ip}/endpoint", data={'value': integer_value})