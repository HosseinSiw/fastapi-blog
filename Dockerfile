FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app .
EXPOSE 8001
CMD [ "python3", "main.py" ]