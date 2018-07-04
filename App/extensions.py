from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from threading import Thread
from flask_mail import Mail
# from flask_login import LoginManager
from flask_login import LoginManager
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()


def extensions_init(app):
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app=app)
    mail.init_app(app)
    login



