from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    contact_info = {
        'email': "ehuang26@nmhschool.org",
        'GitHub': "ethanh26",
        'phone': None
    }
    return render_template("contact.html", **contact_info)

@app.route("/about")
def about():
    about = {
        'food': "chicken alfredo",
        'name': "Ethan",
        'fav_lang': "Javascript"
    }
    return render_template("about.html", **about)

app.run(debug=True)