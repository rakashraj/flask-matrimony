from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
class MessageForm(FlaskForm):
	content=TextAreaField('Content', validators=[DataRequired()])
	submit=SubmitField('Send Proposal')