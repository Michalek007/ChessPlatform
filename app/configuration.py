import os


class Config:
    """App configuration."""
    SERVER_NAME = '127.0.0.1:5000'
    SCHEDULER_API_ENABLED = True
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data.db')
    JWT_SECRET_KEY = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_CSRF_HEADER_NAME = "X-CSRF-TOKEN-ACCESS"
    JWT_COOKIE_CSRF_PROTECT = False
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"
    DEBUG = True
    TESTING = False
