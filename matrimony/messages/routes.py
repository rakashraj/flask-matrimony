from flask import Flask, render_template, url_for, redirect, flash, Blueprint, request
from flask_login import current_user, login_required
from matrimony import db
from matrimony.messages.models import Message
from matrimony.messages.forms import MessageForm
from datetime import datetime

messages=Blueprint('messages', __name__)

@messages.route('/messages/new/<int:reciever>', methods=['GET', 'POST'])
@login_required
def new_message(reciever):
	form=MessageForm()
	if form.validate_on_submit():
		if current_user.id==reciever:
			flash('Bad Request!', 'danger')
			return redirect(url_for('main.home'))
		post=Message(content=form.content.data,
			timing=datetime.utcnow(),
			sender_id=current_user.id, 
			reciever_id=reciever)
		db.session.add(post)
		db.session.commit()
		flash('Your Proposal has been Sent!', 'success')
		return redirect(url_for('main.home'))
	return render_template('send_message.html', form=form, legend='Proposal')

	


@messages.route('/messages/user', methods=['GET'])
@login_required
def user_message():
	page=request.args.get('page', 1, type=int) #1 is default, only int
	messages=Message.query.filter_by(reciever_id=current_user.id).order_by(Message.timing.desc()).paginate(page=page, per_page=2)
	return render_template('messages.html', messages=messages, legend='Proposal')