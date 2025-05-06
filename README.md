# book_managment_app

このプロジェクトは、Dockerの練習用に構築した書籍管理のサンプルアプリケーションです。

## 構成技術

- Frontend, Backend: Flask
- Database: SQLite, SQLAlchemy
- インフラ: Docker

##  学習目的

- dockerを使用してサービスを開発、起動

##  起動方法

### ターミナル
```bash
git clone https://github.com/JerryMuscle/docker_practice_app.git
cd docker_practice_app
docker image build -t (image name) .
docker container run -p 8080:5000 (image name)
```
### 接続
http://localhost:8080/books に接続
- 画面表示(最初は書籍一覧は表示されません。新規登録で書籍を登録すると表示されます)
<img width="1440" alt="スクリーンショット 2025-05-06 10 38 10" src="https://github.com/user-attachments/assets/87056f5c-1b27-4f1e-9afa-582f2e74f8c7" />

###  さらに開発したい場合
```
git clone https://github.com/JerryMuscle/docker_practice_app.git
cd docker_practice_app
docker image build -t (image name) .
docker run -v $(pwd):/book_app -p 8080:5000 (image name)
```
コンテナを起動したまま、開発することができます
