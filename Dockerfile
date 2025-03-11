FROM python:3.12-slim

WORKDIR app/
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update &&  apt upgrade -y && apt install -y libpq-dev && rm -rf /var/cache/apk/
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt

WORKDIR /app/dating/

EXPOSE 8080

CMD ["python3","manage.py","runserver","0.0.0.0:8080","--settings=dating.settings.prod"]
