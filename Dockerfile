FROM python:3.12-alpine

WORKDIR app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk upgrade && apk add libpq-dev && rm /var/cache/apk/*

COPY . .

RUN python3 -m pip install --no-cache-dir --upgrade pip \
    && python3 -m pip install --no-cache-dir -r requirements.txt

WORKDIR /app/dating/

EXPOSE 8080

CMD ["python3","manage.py","runserver","0.0.0.0:8080","--settings=dating.settings.prod"]
