FROM alpine

RUN apk update && \
    apk add --no-cache python3 py3-pip mariadb-dev build-base python3-dev

RUN pip3 install --upgrade pip && \
    pip3 install mysql-connector-python flask flask_cors docker

WORKDIR /cliente
COPY ./main.py .

CMD ["python3", "main.py"]