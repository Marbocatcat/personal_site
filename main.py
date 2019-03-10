#!/bin/env python3

from datetime import datetime 
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '58536585b6d207ca4c42ef1c7012c881'

# Set SQLALCHEMY Instance Location to our site project location.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# Set SQLALCHEMY Instance 
db = SQLAlchemy(app)

# Create SQLAlchemy model/class for both User and the Post.


class User(db.Model):
    # Create db id column and set db as integer, primary_key sets the id as unique for each user.
    id = db.Column(db.Integer, primary_key=True)
    # Create db username and set the db as string with max length set to 20 charachters , set the username to unique, and nullable meands it cannot be empty.
    username = db.Column(db.String(20), unique=True, nullable=False)
    # Create db for email with same setting as username. 
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Create db for image file and set default image.
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # Create db for password.
    password = db.Column(db.String(60), nullable=False)
    # Reference the author from the post class model.
    posts = db.relationship('Post', backref='author', lazy=True)

    # Creates a class and returns itself.
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    # Create Unique ID for the post.
    id = db.Column(db.Integer, primary_key=True)
    # Create title of the post max of 100.
    title = db.Column(db.String(100), nullable=False)
    # Add the date posted to default datetime.
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Add the content.
    content = db.Column(db.Text, nullable=False)
    # Id of the user that authored the post.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
        {
            
            "title": "Python",
            "content": "An Open Source Project that Defined my life",
            "date_posted": "March 9, 2019",
            },
        {
            "title": "You cant Rust that!",
            "content": "Some tips on how to be more productive in Rust",
            "date_posted": "March 19, 2019", 
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
            flash('You have been logged in!', 'is-success' ) 
            return redirect(url_for('home'))
        else:
            flash('Unsuccessfull login!', 'is-danger')
    return render_template('login.html', title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
