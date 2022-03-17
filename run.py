from flask import Flask, render_template, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

user = {
    "tabernacolulteius": generate_password_hash("profetul")
}


posts = [
    {
        'author': 'Vladislav Gabriel',
        'title': 'CARTEA VIETII MIELULUI',
        'content': 'continut',
        'link': 'https://www.facebook.com/100000701825668/videos/329492255884717/',
        'date_posted': 'Feb 27, 2021'
    },
    {
        'author': 'Vladisalv Gabriel',
        'title': 'A SAPTEA OARA UN NOR SE RIDICA',
        'content': 'Continut',
        'link': 'https://www.facebook.com/100000701825668/videos/1152211058749538/',
        'date_posted': 'Feb 20, 2021'
    }
]

@auth.verify_password
def verify_password(username, password):
    if username in user and check_password_hash(user.get(username), password):
        return username


@app.route("/")
@app.route("/archive")
@auth.login_required
def archive():
    return render_template('archive.html', title='arhiva', posts = posts)


@app.route("/home")
@auth.login_required
def home():
    return render_template('home.html')


@app.route("/about")
@auth.login_required
def about():
    return render_template('about.html', title='info')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='contact')


if __name__ == '__main__':
    app.run(debug=True)