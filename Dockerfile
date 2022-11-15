FROM python:3.8

WORKDIR /usr/src/app

COPY titanic_test.csv .
COPY requirements.txt .
COPY main.py .


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn","main:app","--host=0.0.0.0", "--reload"]
