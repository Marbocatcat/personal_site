from flask import render_template, url_for, flash, redirect
from flaskapp import app,  bcrypt
from flaskapp.forms import LoginForm
from flaskapp.models import User
from flask_login import login_user


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
    # Instantiate the LoginForm class.
    form = LoginForm()
    # Use the validate_on_submit method, to validate form submission in login /
    # page.
    if form.validate_on_submit():
        # Instantiate db User model and query email using the form data after /
        # form submission.
        user = User.query.filter_by(email=form.email.data).first()
        # Grab user password from DB and check with the form.password.data /
        # submitted, if they match let the user login.
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login Successfull!', 'is-success')
            # Return back to / if user is successfull.
            return redirect(url_for('home'))
        else:
            flash('Unsuccessfull login!', 'is-danger')
    return render_template('login.html', title="Login", form=form)

    
# TODO: After logging as admin , add a @app.route("/post"). Create a post.html /
# create a Blog form that will talk to DB and will post in the front page.
