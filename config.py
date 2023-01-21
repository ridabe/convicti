import random
import string

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

DEBUG = True

APPNAME = "Convicti"

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@localhost:3306/sale_control"
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'qwertyuiopasdfghjklzxcvbnm123456'