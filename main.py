from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Should be an environment variable
app.config['SECRET_KEY'] = '6bbec13239799c10b4e62df86679bb7e0fc65bc1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Database classes
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True) # Post here refers to class (uppercase)

  def __repr__(self):
    return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # user.id here refers to user table (lowercase)

  def __repr__(self):
    return f"Post('{self.title}','{self.date_posted}')"

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

if __name__ == '__main__':
  app.run(debug=True)