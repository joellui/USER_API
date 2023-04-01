FROM python:3.11

WORKDIR /USER_API/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]