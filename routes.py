from flask import render_template, redirect
from forms import RegisterForm, ItemForm
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
profiles=[
    {"user" : "admin", "password" : "123123", "email" : "abramaana912@gmail.com", "reply" : []}
]
role="admin"

@app.route('/', methods=["GET", "POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('index.html',form=form)

@app.route('/about', methods=["GET", "POST"])
def about():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('about.html',role=role,Team=Team, form=form)

@app.route('/services', methods=["GET", "POST"])
def services():
    items=Item.query.all()
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('services.html', items=items,role=role, form =form)

@app.route('/news', methods=["GET", "POST"])
def news():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('news.html', role=role, news=news1, form=form)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('contact.html', form=form)

@app.route('/profile/<int:profile_id>', methods=["GET", "POST"])
def profile(profile_id):
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('profile.html', profile_id = profile_id, profile=profiles[profile_id], form=form)

@app.route('/add_item', methods=["GET", "POST"])
def add_item(profile_id):
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
    return render_template('add_item.html', form=form, item=item)
