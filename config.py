import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET-KEY') or 'minhachavesecreta'