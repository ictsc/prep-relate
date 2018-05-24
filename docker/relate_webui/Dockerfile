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

# ソースのコピー
COPY ./ /relate-for-ictsc/

# 設定
RUN python manage.py migrate

RUN npm install

# FIXME: gunicronまたはuwsgiサーバで起動するようにする.
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
