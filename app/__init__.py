from dotenv import load_dotenv
from flask import Flask, Response, request, jsonify, json
from flask_marshmallow import Marshmallow as mrs
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)
app.config.from_object('config')

db =SQLAlchemy(app)

mm = mrs(app)

load_dotenv()

from .Routes import routes