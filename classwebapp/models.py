from classwebapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=False, nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_password = db.Column(db.String(60), nullable=False)
    role = db.relationship('Role', backref='user', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.user_name}', '{self.user_email}')"

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    role = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.role}')"

