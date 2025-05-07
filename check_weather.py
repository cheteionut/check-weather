import requests
import json
from sys import argv 

#Create an account on https://weatherstack.com/ and use the provided access key
access_key="PROVIDED_ACCESS_KEY"

if len(argv) < 2 or len(argv) > 3:
    print("Invalid number of arguments")
    exit(1)

if argv[1] != "rain" and argv[1] != "shine":
    print("Invalid value for the first argument; rain/shine are accepted.")
    exit(1)

if len(argv) == 3:
    location = argv[2]
else:
    location = "fetch:ip"

URL = f"https://api.weatherstack.com/current?access_key={access_key}&query={location}"

def check_weather(key):
    try:
        response = requests.get(URL)
        parse_json = json.loads(response.text)
        value = parse_json['current'][key]
        return value
    except Exception as ex:
        print(ex)
    return False

if argv[1] == "rain":
    precip = check_weather('precip')
    print(f'Rain percentage: {precip}')
    if precip <= 5:
        exit(1)

if argv[1] == "shine":
    uvindex = check_weather('uv_index')
    print(f'UV index: {uvindex}')
    if uvindex <= 3:
        exit(1)

