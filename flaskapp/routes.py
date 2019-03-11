from flask import render_template, url_for, flash, redirect
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('content.html', title="Mar Bocatcat", posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'is-success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessfull login!', 'is-danger')
    return render_template('login.html', title="Login", form=form)
