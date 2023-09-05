from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
# from flask_ckeditor import CKEditor
# from datetime import date
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


################ INITS ##################
app = Flask(__name__)



################ ROUTES ##################
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")



################ RUN ##################

if __name__ == "__main__":
    app.run(debug=True, port=9000)
