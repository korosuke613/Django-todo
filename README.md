# Djangoで動くTodoサイト
Djangoアプリを作る際にForkするためのリポジトリ。

## よく使うDjangoコマンド
* 空のアプリケーション作成
  * `django-admin startproject (プロジェクト名)`
* アプリケーション作成
  * `python manage.py startapp (アプリ名)`
* スーパーユーザの作成
  * `python manage.py createsuperuser`
* 開発用のwebサーバ起動
  * `python manage.py runserver`
* マイグレーションファイルの作成
  * `python manage.py makemigrations (アプリ名)`
* 実際のマイグレーションの実施
  * `python manage.py migrate`
* マイグレーションの結果を表示する
  * `python manage.py sqlmigrate (アプリ名) (マイグレーション番号)`
* 特定アプリに対するテストの実施
  * `python manage.py test (アプリ名)`

## よく使うDjangoリファレンス
* [Django 日本語版ドキュメントトップ](https://docs.djangoproject.com/ja/)
* [Django 公式 QyerySet APIリファレンス (モデル層の基本的なAPI)](https://docs.djangoproject.com/ja/1.11/ref/models/querysets/)
* [Django 公式 テンプレート](https://docs.djangoproject.com/ja/1.11/ref/templates/language/)
* [Django manage.pyのコマンド集](https://codelab.website/django-cheat-sheet/)