FROM debian:jessie
MAINTAINER Harvard University FAS Research Computing

RUN apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y \
       build-essential \
       python3 \
       python3-dev \
       python3-pip \
       libpcre3 \
       libpcre3-dev

RUN pip3 install -U pip setuptools wheel

RUN mkdir -p /usr/src/app/deploy
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY deploy/requirements.txt /usr/src/app/deploy/

RUN pip3 --no-cache-dir install -r /usr/src/app/requirements.txt
RUN pip3 --no-cache-dir install -r /usr/src/app/deploy/requirements.txt

COPY . /usr/src/app
RUN pip3 --no-cache-dir install -e /usr/src/app/

RUN apt-get remove -y \
      build-essential \
      libpcre3-dev \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN ln -s /usr/src/app/deploy/start-ariadne-nda.sh /usr/local/bin/

RUN groupadd uwsgi
RUN useradd -r -g uwsgi uwsgi
USER uwsgi

EXPOSE 80

CMD ["/usr/local/bin/start-ariadne-nda.sh"]
