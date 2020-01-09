from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email


users= Blueprint('users', __name__)


# >>> from flask_bcrypt import Bcrypt
# >>> bcrypt=Bcrypt()
# >>> bcrypt.generate_password_hash('testing')
# b'$2b$12$dMjjaXXYRLDDigAq0vd/WOE8oNAYzd7LLFJfZOzIASWHquxEwB/Sy'
# >>> bcrypt.generate_password_hash('testing').decode('utf-8')
# '$2b$12$.tjQVzHj8oRXNeL4P94Ak.JCeXXN3HI67x3KOPW.cmaYl8kBNYBAi'
# >>> hp=bcrypt.generate_password_hash('testing').decode('utf-8')
# >>> hp
# '$2b$12$eSb74PbIQu0BVvLpHGVD3uoq28ISuzYQtqUwCdDMWW72hP/nENpTa'
# >>> bcrypt.check_password_hash(hp,'test')
# False
# >>> bcrypt.check_password_hash(hp,'testing')
# True


@users.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created with username: {form.username.data} ! You Can Login Now.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html',title='Register',form=form)



@users.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash(f'Login Unsuccessful. Please check Email and Password and Try Again !', 'danger')
    return render_template('login.html',title='Login',form=form)



@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@users.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash(f'Your Account Has Been Updated Successfully !', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file=url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html',title='Account', image_file=image_file, form=form)



@users.route('/user/<string:username>')
def user_posts(username):
    page=request.args.get('page', 1, type=int)
    user=User.query.filter_by(username=username).first_or_404()
    posts=Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('user_posts.html', posts=posts, user=user)



@users.route('/reset_password', methods=['GET','POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form=RequestResetForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An Email has been send with instructions to reset your password ! ', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)



@users.route('/reset_password/<token>', methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user=User.verify_reset_token(token)
    if user is None:
        flash('That is an Invalid or Expired token ! ', 'warning')
        return redirect(url_for('users.reset_request'))
    form=ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password=hashed_password
        db.session.commit()
        flash(f'Your Password has been updated! You Can Login Now.', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form) 
