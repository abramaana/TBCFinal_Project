from flask import render_template, redirect, url_for, flash, request
from forms import RegisterForm, ItemForm, LoginForm
from ext import app, db
from models import Item, User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from os import path

Team = [
    {"name": "Nino Kelenjeridze", "image": "nino.png"},
    {"name": "Ana Abramishvili", "image": "ana.png"},
    {"name": "Mariam Bitsadze", "image": "mari.png"}
]

news1 = [
    {"class": "bunny", "name": "BUNNY : hat , dress , overalls(coming soon)",
     "image": ["photo2.png", "new2.png", "new3.png", "new4.png"]},
    {"class": "shoulder", "name": "SHOULDER BAG : colors", "image": ["pr2.png", "new6.png"]},
    {"class": "valentine", "name": "VALENTINE'S BAG : colors", "image": ["pr6.png", "new5.png"]},
]


@app.route('/', methods=["GET", "POST"])
def home():
    formL = LoginForm()
    form = RegisterForm()

    if formL.submit.data and formL.validate():
        user = User.query.filter_by(username=formL.username.data).first()
        if user and user.check_password(formL.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

    if form.submit.data and form.validate():
        new_user = User(
            email=form.email.data,
            username=form.username.data
        )
        new_user.set_password(form.password.data)
        new_user.create()
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))

    return render_template('index.html', form=form, formL=formL)


@app.route('/about', methods=["GET", "POST"])
def about():
    formL = LoginForm()
    form = RegisterForm()

    if formL.submit.data and formL.validate():
        user = User.query.filter_by(username=formL.username.data).first()
        if user and user.check_password(formL.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('about'))
        else:
            flash('Invalid username or password', 'danger')

    if form.submit.data and form.validate():
        new_user = User(
            email=form.email.data,
            username=form.username.data
        )
        new_user.set_password(form.password.data)
        new_user.create()
        flash('Registration successful!', 'success')
        return redirect(url_for('about'))

    return render_template('about.html', Team=Team, form=form, formL=formL)


@app.route('/services', methods=["GET", "POST"])
def services():
    formL = LoginForm()
    form = RegisterForm()

    if formL.submit.data and formL.validate():
        user = User.query.filter_by(username=formL.username.data).first()
        if user and user.check_password(formL.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('services'))
        else:
            flash('Invalid username or password', 'danger')

    if form.submit.data and form.validate():
        new_user = User(
            email=form.email.data,
            username=form.username.data
        )
        new_user.set_password(form.password.data)
        new_user.create()
        flash('Registration successful!', 'success')
        return redirect(url_for('services'))

    items = Item.query.all()
    return render_template('services.html', items=items, form=form, formL=formL)


@app.route('/news', methods=["GET", "POST"])
def news():
    formL = LoginForm()
    form = RegisterForm()

    if formL.submit.data and formL.validate():
        user = User.query.filter_by(username=formL.username.data).first()
        if user and user.check_password(formL.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('news'))
        else:
            flash('Invalid username or password', 'danger')

    if form.submit.data and form.validate():
        new_user = User(
            email=form.email.data,
            username=form.username.data
        )
        new_user.set_password(form.password.data)
        new_user.create()
        flash('Registration successful!', 'success')
        return redirect(url_for('news'))

    return render_template('news.html', news=news1, form=form, formL=formL)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    formL = LoginForm()
    form = RegisterForm()

    if formL.submit.data and formL.validate():
        user = User.query.filter_by(username=formL.username.data).first()
        if user and user.check_password(formL.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Invalid username or password', 'danger')

    if form.submit.data and form.validate():
        new_user = User(
            email=form.email.data,
            username=form.username.data
        )
        new_user.set_password(form.password.data)
        new_user.create()
        flash('Registration successful!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form, formL=formL)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/add_item', methods=["GET", "POST"])
@login_required
def add_item():
    item_form = ItemForm()
    formL = LoginForm()
    form = RegisterForm()

    if item_form.validate_on_submit():
        new_item = Item(
            name=item_form.name.data
        )

        if item_form.image.data:
            image = item_form.image.data
            filename=secure_filename(image.filename)
            save_path= os.path.join(app.root_path, "static", filename)
            image.save(save_path)
            new_item.image = filename

        new_item.create()
        flash('Item added successfully!', 'success')
        return redirect(url_for('services'))

    return render_template('add_item.html', form=form, item=item_form, formL=formL)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


'''@app.route('/create_admin')
def create_admin():
    admin = User.query.filter_by(username='admin').first()
    if admin:
        return "Admin already exists"

    admin = User(
        email='admin@tussaj.com',
        username='admin',
        role='admin'
    )
    admin.set_password('admin123')
    admin.create()
    return "Admin user created successfully"'''