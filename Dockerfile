FROM python:3.9-slim

WORKDIR /home/data

COPY script.py .
COPY IF-1.txt .
COPY AlwaysRememberUsThisWay-1.txt .

RUN mkdir -p /home/data/output

CMD ["python", "script.py"]

