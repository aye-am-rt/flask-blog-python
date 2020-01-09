# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from flask_mail import Mail
# from flaskblog.Config import Config




# db = SQLAlchemy()
# bcrypt = Bcrypt()
# login_manager=LoginManager()
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'
# mail=Mail()

# def prr():
#     print("hello")
#     return True

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)
#     mail.init_app(app)

#     from flaskblog.users.routes import users
#     from flaskblog.posts.routes import posts
#     from flaskblog.main.routes import main
#     app.register_blueprint(users)
#     print("registerd blueprint")
#     app.register_blueprint(posts)
#     app.register_blueprint(main)

#     return app




import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '40595f24c9c5560f4726bf8c2210099a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
app.register_blueprint(users)
print("registerd blueprint")
app.register_blueprint(posts)
app.register_blueprint(main)




# (env) H:\intellijPython\py1\py2>python
# Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# >>> s=Serializer('secret', 90) 
# >>> token=s.dumps({'user_id': 1}).decode('utf-8') 
# >>> token
# 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3NzkwMzEyOSwiZXhwIjoxNTc3OTAzMjE5fQ.eyJ1c2VyX2lkIjoxfQ.P9dMwen_AT5AoU2OaFmDfkxBxOfcOyuxQCBl_NWIhEwsrhSrnyUmFfF8ArjvDydQ1Gx9-AxMUaFoGaBMYgz3cA'
# >>> s.loads(token)
# {'user_id': 1}
# >>> s.loads(token)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "H:\intellijPython\py1\py2\env\lib\site-packages\itsdangerous\jws.py", line 205, in loads
#     date_signed=self.get_issue_date(header),
# itsdangerous.exc.SignatureExpired: Signature expired