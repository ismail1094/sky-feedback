from flask import render_template, Flask
from application import app


@app.route('/')
def home():
    return render_template("home.html", customer_name="Bob", engineer_name="Rob")
