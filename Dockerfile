FROM python:3.7.9-alpine

WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .
COPY main.py .

EXPOSE 5000

ENV ENVIRONMENT local

ENTRYPOINT python main.py