FROM python:3.9.21-slim

COPY check_weather.py .

RUN python3 -m pip install requests

ENTRYPOINT ["python3","./check_weather.py"]
