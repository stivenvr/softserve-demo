FROM alpine:latest

RUN apk add --update python3 py3-pip

COPY app.py app/
COPY requirements.txt app/
COPY templates/index.html app/templates/
COPY templates/styles.css app/templates/

WORKDIR /app


RUN pip install -r requirements.txt

CMD [ "python3", "/app/app.py" ]
