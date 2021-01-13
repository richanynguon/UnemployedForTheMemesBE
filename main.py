from flask import Flask, jsonify
from Flask_SQLAlchemy import SQLAlchemy 
import os


app = Flask(__name__)
# DATABASE_URL = os.getenv('DATABASE_URL`)
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
# db = SQLAlchemy(app)

@app.route('/')
def index():
    msg = "running"
    return jsonify(msg)

if __name__ == '__main__':
    app.run(debug=True)
