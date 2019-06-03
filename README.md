# intern2021_summer_HirakawaSuguru

簡単なマイクロポストAPIです


動作環境
===========

Python 3.7.2

SQLite 3.24.0


始め方
===========
1. プロジェクトのクローン

    `git clone https://github.com/f81/intern2021_summer_HirakawaSuguru.git`

1. プロジェクトフォルダに移動

    `cd fringe_intern/`

1. モジュールのインストール

    `pip install -r requirements.txt`

1. モデルのmigrate

    `python manage.py migrate`

1. fringe_internフォルダ下に `local_settings.py` を作成

1. `local_settings.py` に `SECRET_KEY = '*******'`を追加(SECRET_KEYは作成者に聞いてください)

1. サーバー起動

    `python manage.py runserver`


使い方
===========
APIのエンドポイントは `http://127.0.0.1:8000/api/v1/` です


テスト方法
===========
1. 管理画面からテストユーザーを登録
(管理画面URL: `http://127.0.0.1:8000/admin` Username,Passwordは作成者に聞いてください．)

1. `./check_api_darwin http://127.0.0.1:8000/api/v1/` でテスト実行
