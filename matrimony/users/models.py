from datetime import datetime
from matrimony import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#from matrimony.profiles.models import Profile, About, Family, Partner

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



class User(db.Model, UserMixin):
	id=db.Column(db.Integer , primary_key=True)
	name=db.Column(db.String(50) ,nullable=False)
	email=db.Column(db.String(120), unique=True, nullable=False,)
	last_login=db.Column(db.DateTime, default=datetime.utcnow() , nullable=False)
	password=db.Column(db.String(60), nullable=False)
	profile=db.relationship('Profile', backref='author', uselist=False)
	about=db.relationship('About', backref='user', uselist=False)
	family=db.relationship('Family', backref='user', uselist=False)
	partner=db.relationship('Partner', backref='user', uselist=False)
	message=db.relationship('Message', backref='user', lazy=True)

	def get_reset_token(self, expires_secs=1800):
		s=Serializer(app.config['SECRET_KEY'], expires_secs)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s=Serializer(app.config['SECRET_KEY'])
		try:
			user_id=s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)
	def __repr__(self):
		return "User({}, {})".format(self.name,self.email)
"""

class Profile(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	date_of_birth=db.Column(db.DateTime, nullable=False)
	religion=db.Column(db.Enum('Hindu', 'Muslim', 'Christian', 'Sikh', 'Athiest'), nullable=False)
	maritial_status=db.Column(db.Enum('Single', 'Widow', 'Divorced'), nullable=False)
	gender=db.Column(db.Enum('Male', 'Female'), nullable=False)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
	about=db.relationship('About', backref='profile', uselist=False)
	family=db.relationship('Family', backref='profile', uselist=False)
	partner=db.relationship('Partner', backref='profile', uselist=False)

	def __repr__(self):
		return "Profile({}, {}, {},{})".format(self.date_of_birth,self.religion, self.gender, self.author)


class About(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	mother_tongue=db.Column(db.String(30), nullable=False)
	height=db.Column(db.Float, nullable=False)
	raasi=db.Column(db.String(12), nullable=True)
	weight=db.Column(db.Integer, nullable=True)
	place_of_birth=db.Column(db.String(24), nullable=True)
	edutcation=db.Column(db.String(60), nullable=True)
	occupation=db.Column(db.String(50), nullable=True)
	income=db.Column(db.Integer, nullable=True)
	profile_id=db.Column(db.Integer, db.ForeignKey('profile.id'), unique=True)
	def __repr__(self):
		return "about({})".format(self.mother_tongue)


class Family(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	father=db.Column(db.String(50),nullable=True)
	mother=db.Column(db.String(50), nullable=True)
	sister=db.Column(db.Integer, nullable=True)
	brother=db.Column(db.Integer, nullable=True)
	family_joint=db.Column(db.Enum('yes', 'no'), nullable=True)
	profile_id=db.Column(db.Integer, db.ForeignKey('profile.id') , unique=True)
	def __repr__(self):
		return "Family({})".format(self.family_joint)

class Partner(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	min_age=db.Column(db.Integer, nullable=True, default=20)
	max_age=db.Column(db.Integer, nullable=True, default=60)
	status=db.Column(db.Enum('Single', 'Widow', 'Divorced'), nullable=True)
	complexion=db.Column(db.String(20),nullable=True)
	height=db.Column(db.Integer,nullable=True)
	p_religion=db.Column(db.Enum('Hindu', 'Muslim', 'Christian', 'Sikh', 'Athiest'), nullable=False)
	language=db.Column(db.String(30), nullable=False)
	p_education=db.Column(db.String(60), nullable=True)
	state=db.Column(db.String(20), nullable=True)
	profile_id=db.Column(db.Integer, db.ForeignKey('profile.id') , unique=True)
	def __repr__(self):
		return "partner({})".format(self.status)	"""