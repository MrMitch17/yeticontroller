from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', enviornment=os.environ.get('ENVIRONMENT', 'dev'), version=os.environ.get('VERSION', '0.0.1'))