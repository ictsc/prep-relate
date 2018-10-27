FROM nginx

# Python3実行環境のインストール.
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# ライブラリのインストール.
RUN mkdir /relate-documentation
WORKDIR /relate-documentation/
COPY ./requirements.txt /relate-documentation/
RUN pip3 install -r requirements.txt
COPY ./ /relate-documentation/
RUN make html

ADD deployment/server.conf /etc/nginx/conf.d/default.conf

RUN mkdir /root/logs
RUN mkdir -p /root/public/relate-documentation/
RUN cp -r /relate-documentation/_build/html/* /root/public/relate-documentation/
RUN chmod 755 -R /root

CMD ["nginx", "-g", "daemon off;"]