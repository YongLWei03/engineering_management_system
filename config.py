# --*-- coding:utf-8 --*--

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    ROOT_DIR = os.path.dirname(basedir)
    UPLOAD_FOLDER = "%s/app/static/" % ROOT_DIR

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    '''
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DEV_DATABASE_URL") or
                               "sqlite:///" + os.path.join(
                                   basedir, 'data-dev.sqlite'))
    '''
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DEV_DATABASE_URL") or
                               "mysql://root:@localhost/ems")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DATABASE_URL") or "sqlite:///" +
                               os.path.join(basedir, "data.sqlite"))

config = {
    "development": DevelopmentConfig,
    "prodution": ProductionConfig,

    "default": DevelopmentConfig
}
