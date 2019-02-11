from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='c479bacdd0c74eb9a993db96ab42326e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view='users.login'
login_manager.login_message_category='info'

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='dsfbhhsa@gmail.com'
app.config['MAIL_PASSWORD']='####gbhhghgvfgv'

#from flaskblog import routes some problems
from matrimony.users.routes import users
from matrimony.main.routes import main
from matrimony.profiles.routes import profiles
from matrimony.messages.routes import messages



app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(profiles)
app.register_blueprint(messages)