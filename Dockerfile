FROM alpine:3.17

RUN apk add --update --no-cache python3 py3-pip \
    &&  pip3 install --upgrade pip

WORKDIR /app

COPY . /app/

RUN pip3 --no-cache-dir install -r requirements.txt

CMD [ "python3", "app.py" ]
