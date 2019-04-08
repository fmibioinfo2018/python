FROM ubuntu:16.04

MAINTANER Iliyan Mihaylov "iliqn.mihailov.92@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install flask flask-jsonpify flask-restful neo4j pymongo

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "rest_server.py" ]