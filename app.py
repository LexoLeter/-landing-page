from flask import Flask
from flask import render_template
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)


