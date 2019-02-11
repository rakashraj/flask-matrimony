from datetime import datetime
from matrimony import db, login_manager, app
#from matrimony.users.models import User



class Profile(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	religion=db.Column(db.Enum('Hindu', 'Muslim', 'Christian', 'Sikh', 'Athiest'), nullable=False)
	maritial_status=db.Column(db.Enum('Single', 'Widow', 'Divorced'), nullable=False)
	gender=db.Column(db.Enum('Male', 'Female'), nullable=False)
	date_of_birth=db.Column(db.DateTime, nullable=False)
	age=db.Column(db.Integer, nullable=True)
	image_file=db.Column(db.String(60), default='default.jpg' ,nullable=False)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id'))


	def __repr__(self):
		return "Profile({}, {}, {},{},{})".format(self.date_of_birth,self.religion, self.gender, self.author, self.image_file)
	

class About(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	mother_tongue=db.Column(db.String(30), nullable=False)
	height=db.Column(db.Float, nullable=False)
	weight=db.Column(db.Integer, nullable=True)
	state=db.Column(db.String(20), nullable=True)
	place_of_birth=db.Column(db.String(24), nullable=True)
	education=db.Column(db.String(60), nullable=True)
	occupation=db.Column(db.String(50), nullable=True)
	income=db.Column(db.Integer, nullable=True)
	drink=db.Column(db.Enum('Yes', 'No', ''), nullable=True)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)

	def __repr__(self):
		return "about({})".format(self.mother_tongue)

class Family(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	father_name=db.Column(db.String(50),nullable=True)
	mother_name=db.Column(db.String(50), nullable=True)
	sister=db.Column(db.Integer, nullable=True)
	brother=db.Column(db.Integer, nullable=True)
	family_joint=db.Column(db.Enum('Yes', 'No', ''), nullable=True)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id') , unique=True)
	def __repr__(self):
		return "Family({})".format(self.family_joint)

class Partner(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	min_age=db.Column(db.Integer, default=20)
	max_age=db.Column(db.Integer, default=60)
	status=db.Column(db.Enum('Single', 'Widow', 'Divorced', ''), nullable=True)
	complexion=db.Column(db.String(20),nullable=True)
	p_religion=db.Column(db.Enum('Hindu', 'Muslim', 'Christian', 'Sikh', 'Athiest', ''), nullable=True)
	language=db.Column(db.String(30), nullable=False)
	p_education=db.Column(db.String(60), nullable=True)
	p_state=db.Column(db.String(20), nullable=True)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id') , unique=True)
	def __repr__(self):
		return "partner({})".format(self.status)