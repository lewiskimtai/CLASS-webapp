from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length, ValidationError
from classwebapp.models import Student, Lecturer

class StudentRegistrationForm(FlaskForm):
    student_name = StringField('Student_Name', validators=[Required(), Length(min=2, max=20)])
    student_email = StringField('Student_Email', validators=[Required(), Email()])
    student_password = PasswordField('Student_Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('student_password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        student = Student.query.filter_by(email=student_email.data).first()
        if student:
            raise ValidationError('That email is taken. Please choose a different one.')

class StudentLoginForm(FlaskForm):
    student_email = StringField('Student_Email', validators=[Required(), Email()])
    student_password = PasswordField('Student_Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class LecturerRegistrationForm(FlaskForm):
    lecturer_name = StringField('Lecturer_Name', validators=[Required(), Length(min=2, max=20)])
    lecturer_email = StringField('Lecturer_Email', validators=[Required(), Email()])
    lecturer_password = PasswordField('Lecturer_Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('lecturer_password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        lecturer = Lecturer.query.filter_by(email=lecturer_email.data).first()
        if lecturer:
            raise ValidationError('That email is taken. Please choose a different one.')

class LecturerLoginForm(FlaskForm):
    lecturer_email = StringField('Lecturer_Email', validators=[Required(), Email()])
    lecturer_password = PasswordField('Lecturer_Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(min=2, max=20)])
    email = StringField('Email', validators=[Required(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
