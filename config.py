# --*-- coding:utf-8 --*--

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(config):
    DEBUG = True
    SQLAlCHEMY_DATABASE_URI = (os.environ.get("DEV_DATABASE_URL") or
                               "sqlite:///" + os.path.join(
                                   basedir, 'data-dev.sqlite'))


class ProductionConfig(config):
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DATABASE_URL") or "sqlite:///" +
                               os.path.join(basedir, "data.sqlite"))

config = {
    "development": DevelopmentConfig,
    "prodution": ProductionConfig,

    "default": DevelopmentConfig
}
