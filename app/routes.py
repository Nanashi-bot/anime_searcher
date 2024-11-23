from flask import render_template, request
from app import app
from app.utils import fetch_anime_details

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        anime_name = request.form["anime_name"]
        anime_details = fetch_anime_details(anime_name)
        return render_template("result.html", anime_details=anime_details)
    return render_template("index.html")

