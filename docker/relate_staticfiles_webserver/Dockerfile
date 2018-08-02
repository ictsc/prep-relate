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

RUN npm install

RUN python manage.py collectstatic --noinput
ADD docker/relate_staticfiles_webserver/server.conf /etc/nginx/conf.d/default.conf
RUN mkdir /root/logs
RUN mkdir -p /root/public/relate-static/
RUN cp -r /relate-for-ictsc/static/* /root/public/relate-static/
RUN chmod 755 -R /root
CMD ["nginx", "-g", "daemon off;"]
