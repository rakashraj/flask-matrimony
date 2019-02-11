from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateTimeField, RadioField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Optional, Required, number_range
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
import datetime
maax=datetime.datetime.strptime('1959-01-01 00:00', '%Y-%m-%d %H:%M')
miin=datetime.datetime.strptime('2001-01-01 00:00', '%Y-%m-%d %H:%M')
class ProfileForm(FlaskForm):
	gender=SelectField('Gender', validators=[DataRequired(), Optional()], choices=[('','-------------'),('Male','Male'), ('Female', 'Female')])
	religion=SelectField('Religion', validators=[DataRequired(), Optional()], choices=[('','-------------'),('Hindu','Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Athiest', 'Athiest')])
	maritial_status=SelectField('Maritial Status', validators=[DataRequired()], choices=[('Single','Single'), ('Widow', 'Widow'), ('Divorced', 'Divorced')])
	date_of_birth=DateTimeField('Date of Birth',  validators=[DataRequired(), number_range(maax, miin, message='you should be older then 18 year or younger then 60 year.')] ,format='%Y-%m-%d %H:%M', render_kw={"placeholder":"YYYY-MM-DD HH:MM"})
	picture=FileField('Image', validators=[FileAllowed(['jpg' , 'png'])])
	submit=SubmitField('Create Profile')

class SearchForm(FlaskForm):
	gender=SelectField('Gender', validators=[DataRequired(), Optional()], choices=[('Male','Male'), ('Female', 'Female')])
	religion=religion=SelectField('Religion* : ', validators=[Optional()], choices=[('Hindu','Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Athiest', 'Athiest')])
	maritial_status=SelectField('Maritial Status* : ',validators=[ Optional()], choices=[('Single','Single'), ('Widow', 'Widow'), ('Divorced', 'Divorced')])
	min_age=IntegerField('Age : ', validators=[Optional()])
	max_age=IntegerField('Max Age : ', validators=[Optional()])
	submit=SubmitField('Save')
	

class AaboutForm(FlaskForm):
	picture=FileField('Image', validators=[FileAllowed(['jpg' , 'png']), Optional()])
	maritial_status=SelectField('Maritial Status* : ',validators=[ Optional()], choices=[('Single','Single'), ('Widow', 'Widow'), ('Divorced', 'Divorced')])
	mother_tongue=StringField('Mother Tongue* : ', validators=[DataRequired() ])
	weight=IntegerField('Weight : ', validators=[Optional()])
	height=FloatField('Height* :', validators=[DataRequired()])
	state=StringField('State : ', validators=[ Optional()])
	drink=SelectField('Drink : ', validators=[ Optional()], choices=[("",'-------------'),('Yes','Yes'), ('No', 'No')])
	religion=SelectField('Religion* : ', validators=[Optional()], choices=[('Hindu','Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Athiest', 'Athiest')])
	place_of_birth=StringField('Place of Birth : ', validators=[Optional() ])
	#date_of_birth=DateTimeField('Date of Birth : ', validators=[Optional() ] ,format='%Y-%m-%d %H:%M', render_kw={"placeholder":"YYYY-MM-DD HH:MM"})
	education=StringField('Education Detail :', validators=[Optional()])
	occupation=StringField('Occupation Detail : ', validators=[Optional()])
	income=IntegerField('Annual Income : ', validators=[Optional()])
	father_name=StringField('Father Name : ', validators=[Optional()])
	mother_name=StringField('Mother Name : ', validators=[Optional()])
	sister=IntegerField('No. of Sister : ', validators=[Optional()])
	brother=IntegerField('No. of Brother : ', validators=[Optional()])
	family_joint=SelectField('Joint Family* : ', validators=[ Optional()], choices=[('','-------------'),('Yes','Yes'), ('No', 'No')])
	min_age=IntegerField('Min Age : ', validators=[Optional()])
	max_age=IntegerField('Max Age : ', validators=[Optional()])
	status=SelectField('Maritial Status : ',validators=[ Optional()], choices=[('','-------------'),('Single','Single'), ('Widow', 'Widow'), ('Divorced', 'Divorced')])
	complexion=StringField('Complexion : ', validators=[Optional()])
	p_religion=SelectField('Religion : ', validators=[Optional()], choices=[('','-------------'),('Hindu','Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Athiest', 'Athiest')])
	language=StringField('Mother Tongue* : ', validators=[DataRequired() ])
	p_education=StringField('Education Detain : ', validators=[Optional()])
	p_state=StringField('State : ', validators=[ Optional() ])
	submit=SubmitField('Save')
"""
class EditProfileForm(FlaskForm):
	picture=FileField('Image', validators=[FileAllowed(['jpg' , 'png']), Optional()])
	maritial_status=SelectField('Maritial Status : ',validators=[ ], choices=[('Single','Single'), ('Widow', 'Widow'), ('Divorced', 'Divorced')])
	mother_tongue=StringField('Mother Tongue : ', validators=[DataRequired() ])
	weight=IntegerField('Weight : ', validators=[])
	height=FloatField('Height :', validators=[DataRequired()])
	state=StringField('State : ', validators=[ ])
	drink=SelectField('Drink : ', validators=[ ], choices=[('','-------------'),('Yes','Yes'), ('No', 'No')])
	religion=SelectField('Religion : ', validators=[], choices=[('Hindu','Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Athiest', 'Athiest')])
	place_of_birth=StringField('Place of Birth : ', validators=[Optional() ])
	#date_of_birth=DateTimeField('Date of Birth : ', validators=[Optional() ] ,format='%Y-%m-%d %H:%M', render_kw={"placeholder":"YYYY-MM-DD HH:MM"})
	education=StringField('Education Detain : ', validators=[Optional()])
	occupation=StringField('Occupation Detail : ', validators=[Optional()])
	income=IntegerField('Annual Income : ', validators=[Optional()])
	father_name=StringField('Father Name : ', validators=[Optional()])
	mother_name=StringField('Mother Name : ', validators=[Optional()])
	sister=IntegerField('No. of Sister : ', validators=[Optional()])
	brother=IntegerField('No. of Brother : ', validators=[Optional()])
	family_joint=SelectField('Joint Family : ', validators=[ Optional()], choices=[('','-------------'),('Yes','Yes'), ('No', 'No')])
	
	submit=SubmitField('Save')
class AboutForm(FlaskForm):
	father_name=StringField('Father Name : ', validators=[Optional()])
	mother_name=StringField('Mother Name : ', validators=[Optional()])
	sister=IntegerField('No. of Sister : ', validators=[Optional()])
	brother=IntegerField('No. of Brother : ', validators=[Optional()])
	family_joint=SelectField('Joint Family : ', validators=[ Optional()], choices=[('','-------------'),('Yes','Yes'), ('No', 'No')])
	submit=SubmitField('Save')
class PartnerForm(FlaskForm):
	min_age=IntegerField('Min Age : ', validators=[Optional()])
	max_age=IntegerField('Max Age : ', validators=[Optional()])
	status=SelectField('Maritial Status : ',validators=[ Optional()], choices=[('','-------------'),('Single','Single'), ('Widow', 'Widow'), ('Divorced', 'Divorced')])
	complexion=StringField('Complexion : ', validators=[Optional()])
	p_religion=SelectField('Religion : ', validators=[Optional()], choices=[('','-------------'),('Hindu','Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('Sikh', 'Sikh'), ('Athiest', 'Athiest')])
	language=StringField('Language : ', validators=[DataRequired() ])
	p_education=StringField('Education Detain : ', validators=[Optional()])
	p_state=StringField('State : ', validators=[ Optional() ])
	submit=SubmitField('Save')
"""