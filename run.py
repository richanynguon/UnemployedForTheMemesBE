from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
DATABASE_URL = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", message="Hi")

if __name__ == '__main__':
    app.run(debug=True)
