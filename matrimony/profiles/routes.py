from flask import Blueprint, render_template, flash, redirect, url_for, request
import uuid
from matrimony.users.models import User
from flask_login import login_user, login_required, current_user
from matrimony.profiles.models import Profile, Family, Partner, About
from matrimony.profiles.forms import ProfileForm, AaboutForm, SearchForm
from matrimony import db, app
import datetime
profiles=Blueprint('profiles', __name__)
from PIL import Image
import os

def save_picture(form_picture):
	if form_picture:
		random_hex=uuid.uuid4().hex
		_, f_ext=os.path.splitext(form_picture.filename)
		picture_fn=random_hex + f_ext
		picture_path=os.path.join(app.root_path, 'static/pictures', picture_fn)
		form_picture.save(picture_path)
		output_size=(300, 300)
		i=Image.open(form_picture)
		i.thumbnail(output_size)
		i.save(picture_path)
		return picture_fn
	else:
		return None


@profiles.route('/profiles/create', methods=['GET', 'POST'])
@login_required
def create():
	if current_user.profile:
		flash("you already has been created your Profile!", 'danger')
		return redirect(url_for('main.home'))
	form=ProfileForm()
	if form.validate_on_submit():
		image=save_picture(form.picture.data) if form.picture.data else None
		age=int((datetime.datetime.utcnow()-form.date_of_birth.data).total_seconds()/31557600)
		#age=int(age.total_seconds()/31557600)
		profile= Profile(date_of_birth=form.date_of_birth.data, 
						religion=form.religion.data,
						age=age,
						maritial_status=form.maritial_status.data,
						gender=form.gender.data,
						image_file=image,
						user_id=current_user.id
						)
		db.session.add(profile)
		db.session.commit()
		flash("your profile has been created!", 'success')
		return redirect(url_for('profiles.edit'))
	return render_template('create.html' ,form=form)

@profiles.route('/profiles/myprofile', methods=['GET'])
@login_required
def myprofile():
	if current_user.profile:
		return render_template('myprofile.html')
	else:
		flash("you need to create your Profile first!", 'danger')
		return redirect(url_for('profiles.create'))

@profiles.route('/profiles/<int:id>', methods=['GET'])
def profile(id):
	user=User.query.get_or_404(id)
	if user.profile:
		return render_template('profile.html', user=user)
	flash('Bad Request', "danger")
	return redirect(url_for('main.home'))


@profiles.route('/profiles/search', methods=['GET', 'POST'])
def search():
	page=request.args.get('page', 1, type=int)
	form=SearchForm()
	if form.validate_on_submit():
		if form.min_age.data is None:
			form.min_age.data=19
		if form.max_age.data is None:
			form.max_age.data=60
		users=Profile.query.filter(Profile.maritial_status==form.maritial_status.data,
			Profile.religion==form.religion.data,
			Profile.gender==form.gender.data,
			Profile.age>=int(form.min_age.data),
			Profile.age<=int(form.max_age.data)).paginate(page =page, per_page=5)
		return render_template('search_result.html', users=users)
	return render_template('search.html', form=form)


#######################################################################


@profiles.route('/profiles/edit', methods=['GET', 'POST'])
@login_required
def edit():
	if current_user.profile:
		form=AaboutForm()
		if form.validate_on_submit():
				if form.picture.data:
					picture_file=save_picture(form.picture.data)
					current_user.profile.image_file=picture_file
				current_user.profile.maritial_status=form.maritial_status.data
				current_user.profile.religion=form.religion.data
				if current_user.about:
					about=About.query.filter_by(user_id=current_user.id).first()
					about.mother_tongue=form.mother_tongue.data
					about.height=form.height.data
					about.weight=form.weight.data
					about.state=form.state.data
					about.drink=form.drink.data #None if form.drink.data is "" else 
					about.place_of_birth=form.place_of_birth.data
					about.education=form.education.data
					about.occupation=form.occupation.data
					about.income=form.income.data
					db.session.commit()
				else:
					about= About(mother_tongue=form.mother_tongue.data,
							height=form.height.data,
							weight=form.weight.data,
							state=form.state.data,
							drink=form.drink.data,
							place_of_birth=form.place_of_birth.data,
							education=form.education.data,
							occupation=form.occupation.data,
							income=form.income.data,
							user_id=current_user.id)
					db.session.add(about)
					db.session.commit()
				if current_user.family:
						family=Family.query.filter_by(user_id=current_user.id).first()
						family.father_name=form.father_name.data
						family.mother_name=form.mother_name.data
						family.sister=form.sister.data
						family.brother=form.brother.data
						family.family_joint=form.family_joint.data #None if  is "" else form.family_joint.data
						db.session.commit()
						
						
				else:
						family=Family(father_name=form.father_name.data,
										mother_name=form.mother_name.data,
										sister=form.sister.data,
										brother=form.brother.data,
										family_joint=form.family_joint.data,
										user_id=current_user.id)
						db.session.add(family)
						db.session.commit()
				if current_user.partner:
					partner=Partner.query.filter_by(user_id=current_user.id).first()
					partner.min_age=form.min_age.data
					partner.max_age=form.max_age.data
					partner.status=form.status.data
					partner.complexion=form.complexion.data
					partner.p_religion=form.p_religion.data
					partner.language=form.language.data
					partner.p_education=form.p_education.data
					partner.p_state=form.p_state.data
					db.session.commit()
					flash("you Profile has been Updated!", 'danger')
				else:
					partner=Partner(min_age=form.min_age.data,
								max_age=form.max_age.data,
								status=form.status.data,
								complexion=form.complexion.data,
								p_religion=form.p_religion.data,
								language=form.language.data,
								p_education=form.p_education.data,
								p_state=form.p_state.data,
								user_id=current_user.id)
					db.session.add(partner)
					db.session.commit()
				return redirect(url_for('profiles.myprofile'))				
		elif request.method=='GET':
			form.religion.data=current_user.profile.religion
			form.maritial_status.data=current_user.profile.maritial_status
			if current_user.about:
				form.mother_tongue.data=current_user.about.mother_tongue
				form.height.data=current_user.about.height
				form.weight.data=current_user.about.weight
				form.state.data=current_user.about.state
				form.drink.data=current_user.about.drink
				form.place_of_birth.data=current_user.about.place_of_birth
				form.education.data=current_user.about.education
				form.occupation.data=current_user.about.occupation
				form.income.data=current_user.about.income
			if current_user.family:
				form.mother_name.data=current_user.family.mother_name
				form.father_name.data=current_user.family.father_name
				form.sister.data=current_user.family.sister
				form.brother.data=current_user.family.brother
				form.family_joint.data=current_user.family.family_joint
			if current_user.partner:
				form.min_age.data=current_user.partner.min_age
				form.max_age.data=current_user.partner.max_age
				form.status.data=current_user.partner.status
				form.complexion.data=current_user.partner.complexion
				form.p_religion.data=current_user.partner.p_religion
				form.language.data=current_user.partner.language
				form.p_education.data=current_user.partner.p_education
				form.p_state.data=current_user.partner.p_state
			return render_template('edit3.html', form=form)
		else:
			return render_template('edit3.html', form=form)
	else:
		flash("you need to create your Profile first!", 'danger')
		return redirect(url_for('main.home'))
