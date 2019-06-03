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

1. 移動

    `cd intern2021_summer_HirakawaSuguru/`

1. モジュールのインストール

    `pip install -r requirements.txt`

1. プロジェクトフォルダに移動

    `cd fringe_intern/`

1. `intern2021_summer_HirakawaSuguru/fringe_intern` フォルダ下に `local_settings.py` を作成

1. `local_settings.py` に `SECRET_KEY = '*******'`を追加(SECRET_KEYは作成者に聞いてください)

1. モデルのmigrate

    `python manage.py migrate`

1. サーバー起動

    `python manage.py runserver`


使い方
===========
APIのBaseURLは `http://127.0.0.1:8000/api/v1/` です

例) ポスト一覧を取得するAPI: `http://127.0.0.1:8000/api/v1/posts`


テスト方法
===========
1. `intern2021_summer_HirakawaSuguru/fringe_intern` フォルダ下で以下のコマンドを実行し，管理者ユーザーの作成

    `python manage.py createsuperuser`

1. 管理画面からテストユーザーを登録
(管理画面URL: `http://127.0.0.1:8000/admin`)

1. `./check_api_darwin http://127.0.0.1:8000/api/v1/` でテスト実行
