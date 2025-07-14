from flask import Flask, render_template
from forms import RegisterForm
from wtforms.validators import DataRequired, Email, Length, EqualTo

app = Flask(__name__)
app.config["SECRET_KEY"] = "111"
items=[
    {"name" : "Bunny-20 GEL", "image" : "photo2.png"},
    {"name" : "Dino-15 GEL", "image" : "photo1.png"},
    {"name" : "Duck-15 GEL", "image" : "photo3.png"},
    {"name" : "Hello kitty-20 GEL", "image" : "pr1.png"},
    {"name" : "Red bag with a white bow-30 GEL", "image" : "pr2.png"},
    {"name" : "Pouch with bows-15 GEL", "image" : "pr3.png"},
    {"name" : "Book cover-15 GEL", "image" : "pr4.png"},
    {"name" : "Asymmetrical green top-15 GEL", "image" : "pr5.png"},
    {"name" : "Blue valentine's bag-15 GEL", "image" : "pr6.png"}
]
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
profiles=[]
role="admin"

@app.route('/', methods=["GET", "POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user={ "email" : form.email.data, "username" : form.username.data, "password" : form.password.data }
        profiles.append(new_user)
    return render_template('index.html',form=form)

@app.route('/about')
def about():
    return render_template('about.html',role=role,Team=Team)

@app.route('/services')
def services():
    return render_template('services.html', items=items,role=role)

@app.route('/news')
def news():
    return render_template('news.html', role=role, news=news1)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/profile/<int:profile_id>')
def profile(profile_id):
    return render_template('profile.html', profile_id = profile_id, profile=profiles[profile_id])

if __name__ == '__main__':
    app.run(debug=True)


