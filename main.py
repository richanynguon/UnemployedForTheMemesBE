from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
DATABASE_URL = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    msg = "running"
    return render_template("index.html", title="Home")

@app.route('/favicon.ico', methods=['GET'])
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
