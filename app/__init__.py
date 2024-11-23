from flask import Flask

app = Flask(__name__)

# Import routes after the app is created
from app import routes

