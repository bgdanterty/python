from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)

##CREATE BOOTSTRAP
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the extension
db = SQLAlchemy()
# initialise the app with the extension
db.init_app(app)


class EditMovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    rating = StringField("Rating", validators=[DataRequired()])
    review = StringField("Review")
    submit = SubmitField("Done")
##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

@app.route("/")
def home():
    data = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", movies=data)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = str(form.review.data)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete")
def delete():
    movie_iq = request.args.get("id")
    movie = db.get_or_404(Movie, movie_iq)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():

if __name__ == '__main__':
    app.run(debug=True)
