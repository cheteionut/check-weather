Please read this Readme file before running the script.

This folder contains 2 files: 
	- check_weather.py
	- Dockerfile

The script can be run in 2 ways:
	
1. python3 check_weather.py [rain/shine] [your_location]

Notes:
	- this script must be run using python3
	- the first argument is required and the only accepted values are : rain / shine
	- the second argument is optional; you can provide your location (e.g. London) or if this argument is not provided the location will be checked based on your IP address

2. docker build --no-cache -t NAME_IT .
   docker run -it NAME_IT [rain/shine] [London]
Note:
	- this Dockerfile must be run using docker
	- the first argument is required and the only accepted values are : rain / shine
	- the second argument is optional; you can provide your location (e.g. London) or if this argument is not provided the location will be checked based on your IP address

