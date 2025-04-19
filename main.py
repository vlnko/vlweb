import os
from flask import Flask, render_template, send_from_directory
from context_processors import get_current_year


app = Flask(__name__)


# Getting the favicon
@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png', mimetype='image/png')


# Passing current year to all templates
@app.context_processor
def inject_year_processor():
    return {'year': get_current_year()}


@app.route("/")
def home_page():
    return render_template("home.html")


if __name__ == '__main__':
	app.run(debug=False)