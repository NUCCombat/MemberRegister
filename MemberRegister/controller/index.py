from flask import render_template

from .. import app


@app.route("/")
def page_index():
    return render_template("index.html")
