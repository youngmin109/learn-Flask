from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# migrate는 Flask-Migrate의 인스턴스 
# migrate는 데이터베이스 스키마 변경을 관리하는 도구
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__) # __name__은 현재 모듈의 이름을 나타냄
    app.config.from_object(config) # config.py 파일에서 설정을 불러옴

    # ORM(Object-Relational Mapping)은 
    # 객체 지향 프로그래밍과 관계형 데이터베이스를 연결하는 기술
    db.init_app(app)
    migrate.init_app(app, db) 
    from . import models

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app