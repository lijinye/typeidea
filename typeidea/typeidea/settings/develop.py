from .base import *   #NOQA

DEBUG = True
import pymysql

pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'typeidea',  # 数据库名，先前创建的
        'USER': 'root',  # 用户名，可以自己创建用户
        'PASSWORD': '',  # 密码
        'HOST': 'localhost',  # mysql服务所在的主机ip
        'PORT': '3306',
        'TEST': {
            'NAME': 'test_db'
        }
    }
}
