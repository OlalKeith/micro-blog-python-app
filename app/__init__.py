from flask import Flask

# this app variable is imported i.e from app import app
app = Flask(__name__)

from app import routes