from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
from dotenv import load_dotenv
import os

load_dotenv()
tmdb_api_key = os.environ["TMDB_API_KEY"]
tmdb_token = os.environ["TMDB_TOKEN"]
api_endpoint = os.environ["API_ENDPOINT"]
movie_db_image_url = "https://image.tmdb.org/t/p/original/"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)
# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    description: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    review: Mapped[str] = mapped_column(String, unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(String, unique=False, nullable=False)


class RateMovieForm(FlaskForm):
    rating = StringField("Your rating out of 10 e.g 7.5", validators=[DataRequired()])
    review = StringField("Your review", validators=[DataRequired(), Length(min=1, max=75)])
    submit = SubmitField("Done")


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].rating = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie,movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

header = {
    "accept": "application/json",
    "Authorization": f"Bearer {tmdb_token}"
}


@app.route("/add", methods=["POST", "GET"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(url=api_endpoint, params={"query": movie_title}, headers=header)
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

details_header = {
    "accept": "application/json",
    "Authorization": f"Bearer {tmdb_token}"
}


@app.route("/find", methods= ["POST", "GET"])
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_details_api_endpoint = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response = requests.get(url=movie_details_api_endpoint, params={"language": "en-US"}, headers=details_header)
        data= response.json()
        new_movie = Movie(title=data["title"],
                          year= data["release_date"].split("-")[0],
                          img_url =f"{movie_db_image_url}{data["poster_path"]}",
                          description=data["overview"])
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
