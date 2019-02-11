from flask import render_template, url_for, redirect, flash, request , Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from passlib.hash import pbkdf2_sha512
from matrimony import db
import datetime
from matrimony.users.models import User
from matrimony.users.forms import RegistrationForm, LoginForm



users=Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password=pbkdf2_sha512.encrypt(form.password.data)
		user= User(name=form.name.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash("your account has been created! you are now able to log in", 'success')
		return redirect(url_for('users.login'))
	return render_template('register.html' ,form=form)

@users.route('/login', methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and pbkdf2_sha512.verify(form.password.data, user.password):
			login_user(user, remember=form.remember.data)
			user.last_login=datetime.datetime.utcnow()
			db.session.commit()
			next_page=request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('main.home'))
		else:
			flash("Login Unsuccessful", 'danger')
	return render_template('login.html', title='Login', form=form)


@users.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return redirect(url_for('main.home'))