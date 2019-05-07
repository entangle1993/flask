from flask import render_template, flash, redirect, url_for,request
from app import app
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User
from werkzeug.urls import url_parse
from app import db
from app.forms import LoginForm,RegistrationForm,EditProfileForm
from datetime import datetime

#上次访问时间
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required #未验证不能访问
def index():
    user = {'username': '台哥'}
    posts = [
        {
            'author': {'username': '撒库yin'},
            'body': '城里的月光把梦照亮，请温暖她心房'
        },
        {
            'author': {'username': 'さくpopo'},
            'body': '好无聊啊'
        }
    ]
    return render_template('index.html', title='Home', posts=posts) #delete user =user
    #render_template的功能是对先引入index.html，同时根据后面传入的参数，对html进行修改渲染。


@app.route('/login', methods=['GET', 'POST'])
def login():
    #登录视图功能逻辑
    if current_user.is_authenticated:
        return redirect(url_for('index'))  #已登录用户
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        #how to read and process the next query string argument:
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        #return redirect(url_for('index'))
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
    return render_template('login.html',  title='Sign In', form=form)

#注销
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
#注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('おめでとう、注册成功した！\(^o^)/~')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#用户个人资料查看
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': '城里的月光'}
    ]
    return render_template('user.html', user=user, posts=posts)

#编辑个人资料的视图函数
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)