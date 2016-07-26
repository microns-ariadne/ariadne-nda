FROM python:3.5.1-slim

# Installs
RUN apt-get update
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Development
RUN mkdir /source
WORKDIR /source
