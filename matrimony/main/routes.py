from flask import render_template, request, Blueprint
from matrimony.users.models import User
main=Blueprint('main', __name__)

@main.route('/')
def home():
	page=request.args.get('page', 1, type=int) #1 is default, only int
	users=User.query.order_by(User.last_login.desc()).paginate(page =page, per_page=5)
	return render_template('home.html', users=users)


@main.route('/credit')
def credit():
	return render_template('credit.html')