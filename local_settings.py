# 環境に応じてロードする設定ファイルを変更する.
import os

if os.environ['DEPLOYMENT_ENV'] == 'production':
    from production_settings import *
elif os.environ['DEPLOYMENT_ENV'] == 'training':
    from training_settings import *
elif os.environ['DEPLOYMENT_ENV'] == 'staging':
    from staging_settings import *
elif os.environ['DEPLOYMENT_ENV'] == 'development':
    from development_settings import *
else:
    from development_settings import *