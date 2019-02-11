from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from matrimony.users.models import User

class RegistrationForm(FlaskForm):
	email=StringField('Email', 
						validators=[DataRequired(), Email()])
	name=StringField('Name', validators=[DataRequired() , Length(min=3 , max=50)])
	password=PasswordField('Password', 
						validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password', 
						validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Sign  Up')
	
	def validate_name(self, name):
		pass

	def validate_email(self, email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('The email is taken. Please choose a diffrent One.')


class LoginForm(FlaskForm):
	email=StringField('Email', 
						validators=[DataRequired(), Email()])
	password=PasswordField('Password', 
						validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	email=StringField('Email', 
						validators=[DataRequired(), Email()])
	picture=FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
	submit=SubmitField('Sign  Up')
	

	def validate_username(self, username):
		if username.data !=current_user.username:
			user=User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a diffrent One.')
		
	def validate_email(self, email):
		if email.data !=current_user.email:
			user=User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('The email is taken. Please choose a diffrent One.')


class RequestResetForm(FlaskForm):
	email=StringField('Email', 
						validators=[DataRequired(), Email()])
	submit=SubmitField('Request Passwrod Reset')
	
	def validate_email(self, email):
		user=User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('Their is no account with that email.')

class ResetPasswordForm(FlaskForm):
	password=PasswordField('Password', 
						validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password', 
						validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Reset Passwrod')
