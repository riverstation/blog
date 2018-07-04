import os
class Config:
    SECRET_KEY = 'abcdef'
    BOOTSTRAP_SERVER_LOCAL = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER= os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME', 'liweiriver@163.com')
    MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD', 'liwei123')


#开发环境
class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@127.0.0.1:3306/dev_blog'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@127.0.0.1:3306/dev-blog'
    DEBUG = True


#测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@127.0.0.1:3306/test-blog'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@127.0.0.1:3306/dev-blog'
    DEBUG = False

#生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@127.0.0.1:3306/blog'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rock1204@127.0.0.1:3306/dev-blog'
    DEBUG = False

config = {
    'production':ProductionConfig,
    'testing':TestingConfig,
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}



