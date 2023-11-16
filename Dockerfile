FROM ubuntu

RUN apt-get clean && apt-get update -y
RUN apt-get -y install python3 pip libpq-dev

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY src src

ENTRYPOINT python3 src/simple_messenger/manage.py migrate && python3 src/simple_messenger/manage.py runserver 0.0.0.0:${SERVICE_PORT}