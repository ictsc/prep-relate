.. include:: ../../definition.txt

運用者向けガイド
======================================

初期設定(DB)
--------------------------------------

1.DBにユーザとDBを作成し、作成したユーザに権限を付与します。

※psqlコマンドなどで、DBにログインします。

.. code-block:: bash

    ictsc=> CREATE ROLE relate WITH LOGIN PASSWORD 'passsword';
    CREATE ROLE
    ictsc=> CREATE DATABASE relate;
    CREATE DATABASE
    ictsc=> GRANT ALL ON DATABASE relate TO relate ;
    GRANT

2.local_settings.pyでimportしている設定ファイルを初期設定を行う対象の環境に切り替えDBパスワードを入力します。

.. code-block:: python

    # 環境に応じてロードする設定ファイルを変更する.
    from development_settings import *

.. csv-table::
   :header: 環境名, ファイル名
   :widths: 5, 5

    本番, production_settings
    ステージング, staging_settings
    開発, development_settings

'PASSWORD': ''となっている部分の''の部分にDBパスワードを入力します。

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'relate',
            'USER': 'relate',
            'PASSWORD': '',
            'HOST': 'db.prep-***.icttoracon.net',
            'PORT': '5432',
        }
    }

3.以下のコマンドを実行します.

.. code-block:: bash

    python manage.py migrate

4.以下のコマンドを実行し管理者ユーザを作成します。

.. code-block:: bash

    python manage.py createsuperuser --username=ictsc-admin

ローカル実行方法
--------------------------------------

1.以下のコマンドを実行します.

.. code-block:: bash

    sh docker_build.sh

2.以下のコマンドを実行します.

.. code-block:: bash

    docker run -p 80:8000 -it relate-webui

3.ブラウザで、http://localhostにアクセスできることを確認します。

デプロイメント
--------------------------------------

1.local_settings.pyでimportしている設定ファイルを本番環境に切り替えDBパスワードを入力します。

.. code-block:: diff

    # 環境に応じてロードする設定ファイルを変更する.
    -from development_settings import *
    +from production_settings import *

'PASSWORD': ''となっている部分の''の部分にDBパスワードを入力します。

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'relate',
            'USER': 'relate',
            'PASSWORD': '',
            'HOST': 'db.prep-***.icttoracon.net',
            'PORT': '5432',
        }
    }

2.以下のコマンドを実行します.

.. code-block:: bash

    sh docker_build.sh

3.k8sのNodeにログインし、以下のコマンドを実行します。

.. code-block:: bash

    vi relate.yaml

以下の内容を入力し保存します。

.. code-block:: yaml

    apiVersion: v1
    kind: Service
    metadata:
      name: relate-service
    spec:
      type: ClusterIP
      ports:
      - name: relate
        port: 80
        targetPort: 7777
        protocol: TCP
      selector:
        app: relate

    ---
    apiVersion: v1
    kind: Pod
    metadata:
      name: relate
      labels:
        app: relate
    spec:
      #volumes:
      #  - name: test
      #    persistentVolumeClaim:
      #      claimName: test
      containers:
      - name: relate
        image: relate-webui:20180524
        ports:
        - name: relate
          containerPort: 7777
          protocol: TCP
    #    volumeMounts:
    #      - mountPath: "/etc/kong"
    #        name: kong-pv-storage

4.以下のコマンドを実行します。

.. code-block:: bash

    kubectl create -f relate.yaml

5.以下のコマンドを実行し、relateのSTATUSがRunningになっていることを確認します。

.. code-block:: bash

    # kubectl get all
    NAME                   READY     STATUS      RESTARTS   AGE
    kong-migration-ddd6x   0/1       Completed   0          9d
    kong-pod               1/1       Running     0          9d
    postgres-jlxwk         1/1       Running     0          9d
    pstate                 1/1       Running     1          8d
    relate                 1/1       Running     0          2m

    NAME       DESIRED   CURRENT   READY     AGE
    postgres   1         1         1         9d

    NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)         AGE
    kong-admin       ClusterIP   10.103.46.233    <none>        8001/TCP        9d
    kong-admin-ssl   ClusterIP   10.110.125.185   <none>        8444/TCP        9d
    kong-proxy       NodePort    10.103.128.212   <none>        80:30854/TCP    9d
    kong-proxy-ssl   NodePort    10.108.68.220    <none>        443:30898/TCP   9d
    kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP         11d
    postgres         ClusterIP   10.111.204.103   <none>        5432/TCP        9d
    pstate-service   ClusterIP   10.108.166.135   <none>        80/TCP          8d
    relate-service   ClusterIP   10.99.15.30      <none>        7777/TCP        2m

    NAME             DESIRED   SUCCESSFUL   AGE
    kong-migration   1         1            9d

5.4で状態を確認した後に、以下のコマンドを実行します。

.. code-block:: bash

    kubectl create -f relate.yaml

    KONG_API_IP=$(kubectl get all | grep kong-admin-ssl | awk '{print $3;}')
    # relate本体のKong設定
    curl -k -i -X POST --url https://$KONG_API_IP:8444/services --data 'name=relate-svc' --data 'url=http://relate-service.default.svc.cluster.local'
    curl -k -i -X POST --url https://$KONG_API_IP:8444/apis -d 'name=relate' -d 'upstream_url=http://relate-service.default.svc.cluster.local/relate' -d 'hosts=prep-dev.icttoracon.net' -d 'uris=/relate'
    # relateドキュメントのKong設定
    curl -k -i -X POST --url https://$KONG_API_IP:8444/services --data 'name=relate-doc-svc' --data 'url=http://relate-documentation-service.default.svc.cluster.local'
    curl -k -i -X POST --url https://$KONG_API_IP:8444/apis -d 'name=relate-doc' -d 'upstream_url=http://relate-documentation-service.default.svc.cluster.local/relate-documentation/' -d 'hosts=prep-dev.icttoracon.net' -d 'uris=/relate-documentation/'


6.ブラウザで「|RELATE_TOP_URL_DEVELOPMENT|」にアクセスし、ページが表示できることを確認します。