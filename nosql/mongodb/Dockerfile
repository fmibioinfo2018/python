FROM       ubuntu:16.04
MAINTAINER Docker

# Installation:
RUN apt-get update && apt-get install -y build-essential python2.7 
RUN apt-get install -y python-setuptools
RUN apt-get install -y python-pip
RUN apt-get install -y nano
RUN apt-get install -y telnet
RUN apt-get install -y vim

# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list

# Update apt-get sources AND install MongoDB
RUN apt-get update && apt-get install -y mongodb-org

# Create the MongoDB data directory
RUN mkdir -p /data/db

# Create the MongoDB data directory
RUN mkdir -p /data/code

RUN pip install bottle

RUN pip install pymongo

# Expose port #27017 from the container to the host
EXPOSE 27017

# Set /usr/bin/mongod as the dockerized entry-point application
ENTRYPOINT ["/bin/bash"]