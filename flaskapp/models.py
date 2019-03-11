from datetime import datetime
from flaskapp import db, login_manager
from flask_login import UserMixin

# This function need to be in place for the login_manager extension to work.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Create SQLAlchemy model/class for both User and the Post.
class User(db.Model, UserMixin):
    # Create db id column and set value type as "integer", primary_key sets the
    # entry as unique.
    id = db.Column(db.Integer, primary_key=True)
    # Create db username and set the db as string with max length set to 20 cha
    # - rachters , set the username to unique, and nullable meands it cannot be
    # - empty.
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
