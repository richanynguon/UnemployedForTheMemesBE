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
    print('I am running index')
    return jsonify(msg)

@app.route('/favicon.ico')
def favicon():
    print("I am running favicon")
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
