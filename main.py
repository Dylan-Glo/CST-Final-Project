from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template('template.html')

