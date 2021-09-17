from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

# Test posts
posts = [
  {
    'author': 'Jebediah Kerman',
    'title': 'Snacks',
    'content': "We didn't bring enough snacks.",
    'date_posted': 'Aug 10, 2021'
  },
  {
    'author': 'Valentina Kerman',
    'title': 'Piloting',
    'content': "Pro tip: Keep the pointy end up.",
    'date_posted': 'Aug 15, 2021'
  }
]

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'JMcDade42@gmail.com' and form.password.data =='itsasecret':
      flash(f'{form.email.data} successfully logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Failed', 'danger')
  return render_template('login.html', title="Login", form=form)