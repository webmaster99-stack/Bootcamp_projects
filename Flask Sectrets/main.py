from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "vg563~.B"

class MyForm(FlaskForm):
    email = StringField(label="email", validators=[DataRequired(), Email()])
    password = PasswordField(label="password", validators=[DataRequired(), Length(min=8, message="Field must be at least 8 characters long")])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods= ["POST", "GET"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
