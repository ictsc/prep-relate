FROM ubuntu:16.04

# Python3実行環境のインストール.
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev curl nginx git vim \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Install Node.js
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install --yes nodejs
RUN apt-get install --yes build-essential


# ライブラリのインストール.
RUN mkdir /relate-for-ictsc
WORKDIR /relate-for-ictsc/
COPY ./requirements.txt /relate-for-ictsc/
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

# ソースのコピー
COPY ./ /relate-for-ictsc/

RUN npm install

RUN python manage.py collectstatic --noinput
# CMD ["uwsgi","-p","10","--http",":7777","--file","/relate-for-ictsc/relate/wsgi.py"]
CMD ["gunicorn", "relate.wsgi", "-b", "0.0.0.0:7777", "-w", "10", "--timeout", "30", "--graceful-timeout", "20", "--max-requests", "1000", "--max-requests-jitter", "500", "--backlog", "500", "--access-logfile", "-", "--error-logfile", "-"]