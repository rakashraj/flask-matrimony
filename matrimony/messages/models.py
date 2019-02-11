from matrimony import db

class Message(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	content=db.Column(db.Text ,nullable=False)
	timing=db.Column(db.DateTime, nullable=False)
	reciever_id=db.Column(db.Integer,  unique=False)
	sender_id=db.Column(db.Integer, db.ForeignKey('user.id') , unique=False)

	def __repr__(self):
		return "Message({})".format(self.content)