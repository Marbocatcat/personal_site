#!/bin/env python3

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def main():
    return render_template('landing.html', title="Blog | Mar Bocatcat")


if __name__ == "__main__":
    app.run(debug=True)
