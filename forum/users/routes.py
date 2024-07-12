from flask import Blueprint, render_template, redirect, url_for, flash, session,jsonify
from forum.users.models import User, Code, Follow
from forum.users.forms import UserRegistrationForm, UserCodeVerifyForm, UserLoginForm, EmptyForm
from forum.extensions import db, sms_api
import random
import datetime


blueprint = Blueprint('users', __name__)


@blueprint.route('/register', methods=['post', 'get'])
def register():
	form = UserRegistrationForm()
	if form.validate_on_submit():
		rand_num = random.randint(1000, 9999)
		session['user_phone'] = form.phone.data
		params = {'sender':'', 'receptor':int(form.phone.data), 'message':rand_num}
		sms_api.sms_send(params)
		code = Code(
					number=rand_num,
					expire=datetime.datetime.now() + datetime.timedelta(minutes=10),
					phone=form.phone.data
					)
		db.session.add(code)
		db.session.commit()
		return jsonify({"message":"send code to your phone"})
	return jsonify({"message":"phone is uncorrect"})


@blueprint.route('/verify', methods=['post', 'get'])
def verify():
	user_phone = session.get('user_phone')
	code = Code.query.filter_by(phone=user_phone).first()
	form = UserCodeVerifyForm()
	if form.validate_on_submit():
		if code.expire < datetime.datetime.now():
			flash('Expiration Error, please try again', 'danger')
			return jsonify({"message":"Expiration Error, please try again"})

		if form.code.data != str(code.number):
			flash('your code is wrong', 'danger')
		else:
			user = User(phone=user_phone)
			db.session.add(user)
			db.session.commit()
			flash('your account created successfully', 'info')
			return jsonify({"message":"get token"})

	return jsonify({"message":"your code is wrong, please try again"})
