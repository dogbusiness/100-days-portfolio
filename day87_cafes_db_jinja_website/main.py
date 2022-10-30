from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Bootsrap Initialisation #
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# SQLAlchemy #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Cafes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    wifi = db.Column(db.String(100))

#WTForm
class AddCafeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    wifi = StringField("Wifi", validators=[DataRequired()])
    submit = SubmitField("Submit New")

# Создай, если удалил, базу
# db.create_all()

# Pages #
@app.route("/")
def home():
    cafes = db.session.query(Cafes).order_by(Cafes.id).all()
    return render_template("index.html", cafes=cafes)

@app.route('/add-cafe', methods=['GET', 'POST'])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        name = form.name.data
        wifi = form.wifi.data
        new_cafe = Cafes(name=name, wifi=wifi)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("cafe-form.html", form=form)

if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=False)

