from classwebapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(student_id):
    return Student.query.get(int(student_id))

@login_manager.user_loader
def load_user(lecturer_id):
    return Student.query.get(int(lecturer_id))

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(20), unique=False, nullable=False)
    student_email = db.Column(db.String(120), unique=True, nullable=False)
    student_password = db.Column(db.String(60), nullable=False)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default=False)
    role = db.relationship('Role', secondary='UserRole', backref=db.backref('student', lazy='dynamic'))

    def __repr__(self):
        return f"User('{self.student_name}', '{self.student_email}')"

class Lecturer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    lecturer_name = db.Column(db.String(20), unique=False, nullable=False)
    lecturer_email = db.Column(db.String(120), unique=True, nullable=False)
    lecturer_password = db.Column(db.String(60), nullable=False)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default=True)
    role = db.relationship('Role', secondary='UserRole', backref=db.backref('lecturer', lazy='dynamic'))
    

    def __repr__(self):
        return f"User('{self.lecturer_name}', '{self.lecturer_email}')"


class Role(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.role_id}')"

class UserRole(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))
    student_id = db.Column(db.Integer(), db.ForeignKey('student.id', ondelete='CASCADE'))
    lecturer_id = db.Column(db.Integer(), db.ForeignKey('lecturer.id', ondelete='CASCADE'))

    def __repr__(self):
        return f"User('{self.role_id}', '{self.student_id}', '{self.lecturer_id}')"

