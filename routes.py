from flask import render_template, redirect
from forms import RegisterForm, ItemForm, LoginForm
from ext import app, db
from models import Item
from wtforms.validators import DataRequired, Email, Length, EqualTo

Team=[
    {"name" : "Nino Kelenjeridze", "image" : "nino.png"},
    {"name" : "Ana Abramishvili", "image" : "ana.png"},
    {"name" : "Mariam Bitsadze", "image" : "mari.png"}
]
news1=[
    {"class" : "bunny", "name" : "BUNNY : hat , dress , overalls(coming soon)" , "image" : ["photo2.png" , "new2.png", "new3.png", "new4.png"]},
    {"class" : "shoulder", "name" : "SHOULDER BAG : colors" , "image" : ["pr2.png" , "new6.png"]},
    {"class" : "valentine", "name" : "VALENTINE'S BAG : colors" , "image" : ["pr6.png" , "new5.png"]},
]
role="admin"

@app.route('/', methods=["GET", "POST"])
def home():
    formL = LoginForm()
    if formL.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        check_pass = user.check_password(form.password.data)
        if user and check_pass:
            login_user(user)
            return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('index.html',form=form, formL=formL)

@app.route('/about', methods=["GET", "POST"])
def about():
    formL = LoginForm()
    if formL.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        check_pass = user.check_password(form.password.data)
        if user and check_pass:
            login_user(user)
            return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('about.html',role=role,Team=Team, form=form, formL=formL)

@app.route('/services', methods=["GET", "POST"])
def services():
    formL = LoginForm()
    if formL.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        check_pass = user.check_password(form.password.data)
        if user and check_pass:
            login_user(user)
            return redirect("/")
    items=Item.query.all()
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('services.html', items=items,role=role, form =form, formL=formL)

@app.route('/news', methods=["GET", "POST"])
def news():
    formL = LoginForm()
    if formL.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        check_pass = user.check_password(form.password.data)
        if user and check_pass:
            login_user(user)
            return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('news.html', role=role, news=news1, form=form, formL=formL)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    formL = LoginForm()
    if formL.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        check_pass = user.check_password(form.password.data)
        if user and check_pass:
            login_user(user)
            return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('contact.html', form=form, formL=formL)

@app.route('/profile/<int:profile_id>', methods=["GET", "POST"])
def profile(profile_id):
    formL = LoginForm()
    if formL.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        check_pass = user.check_password(form.password.data)
        if user and check_pass:
            login_user(user)
            return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('profile.html', profile_id = profile_id, profile=profiles[profile_id], form=form, formL=formL)

@app.route('/add_item', methods=["GET", "POST"])
def add_item(profile_id):
    formL = LoginForm()
    if formL.validate_on_submit():
        user = User.query.filter(form.username.data == User.username).first()
        check_pass = user.check_password(form.password.data)
        if user and check_pass:
            login_user(user)
            return redirect("/")
    item=ItemForm()
    form = RegisterForm()
    if item.validate_on_submit():
        new_item=Item(name=item.name.data)
        image = item.image.data
        directory = path.join(app.root_path, "static", image.filename)
        image.save(directory)
        new_item.image = image.filename
        db.session.add(new_item)
        bd.session.commit()
        return redirect("/services")
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('add_item.html', form=form, item=item, formL=formL)
