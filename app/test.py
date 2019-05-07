from werkzeug.security import generate_password_hash
from app.models import User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from app import app, db
'''
flask shell
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
App: app [production]
Instance: /Users/lu/Documents/Code/microblog/flask/instance
>>> from app import app, db
>>> from app.models import User, Post
>>> db  
<SQLAlchemy engine=sqlite:////Users/lu/Documents/Code/microblog/flask/app.db>
>>> User
<class 'app.models.User'>
>>> Post
<class 'app.models.Post'>
>>> 

'''
# u = User(username='susan', email='susan@example.com')
# u.set_password('cat')
# db.session.add(u)
# db.session.commit()  #添加用户
users = User.query.all() #查看所有用户
print(users[2].about_me)

