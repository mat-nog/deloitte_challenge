from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False