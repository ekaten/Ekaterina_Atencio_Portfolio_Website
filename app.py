from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
import smtplib
from flask_ckeditor import CKEditor
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
import datetime as dt

# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
# from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
# from forms import CreatePostForm, CommentForm
# from flask_gravatar import Gravatar
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Length, Email
# from functools import wraps
# import os

now = dt.datetime.now()
year = now.year

################ INITS ##################
app = Flask(__name__)
app.secret_key = "dfgjsdkgjslkdjglk"
Bootstrap(app)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)


################ FORM CLASSES ##############


class CreateContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired(), Email()])
    message = TextAreaField(validators=[DataRequired()])
    send = SubmitField('Send')


################ ROUTES ##################


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", year=year)


@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("about.html", year=year)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = CreateContactForm()
    if form.validate_on_submit():
        print('Submitted')
        sender = form.name.data
        semder_email = form.email.data
        sent_message = form.message.data
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                my_email = "tenciokatya@gmail.com"
                pswd = "jyojeavwcxjrpxsw"
                connection.starttls()
                connection.login(user=my_email, password=pswd)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="ekaterinaatencio@gmail.com",
                    msg=f'Subject: {sender} sent you a message\n\n{sent_message}\n\n{sender}\n{semder_email}'
                )
        except:
            print("Message couldn't be sent")
            success = False
        else:
            success = True
            message = "Thank you for reaching out!\nI will get back to you as soon as possible\n-Ekaterina Atencio"

        return render_template("contact.html", success=success, year=year)
    else:
        return render_template("contact.html", form=form, year=year)


@app.route('/projects', methods=["GET", "POST"])
def projects():
    return render_template("projects.html", year=year)


@app.route('/skills', methods=["GET", "POST"])
def skills():
    return render_template("skills.html", year=year)


@app.route('/morse', methods=['GET', "POST"])
def morse():
    return render_template("morse.html", year=year)


################ RUN ##################


if __name__ == "__main__":
    app.run()
