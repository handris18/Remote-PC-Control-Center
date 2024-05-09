FROM python:3.12.3

RUN apt-get update -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

EXPOSE 5000

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# CMD ["python", "-m", "flask", "--app", "main_app", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "-w", "2", "--bind", "0.0.0.0:5000", "wsgi:app"]