from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(debug=True)