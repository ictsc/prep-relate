FROM ubuntu:16.04

# Python3実行環境のインストール.
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev curl nginx git \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# ライブラリのインストール.
RUN mkdir /relate-for-ictsc
WORKDIR /relate-for-ictsc/
COPY ./requirements.txt /relate-for-ictsc/
RUN pip3 install -r requirements.txt

# ソースのコピー
RUN apt-get install -y vim
COPY ./ /relate-for-ictsc/

# 設定
RUN cp local_settings_example.py local_settings.py
RUN python manage.py migrate
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
