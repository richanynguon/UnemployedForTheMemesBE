from flask import Flask
from Flask_SQLAlchemy import SQLAlchemy 
import os

app = Flask(__name__)
DATABASE_URL = os.getenv('DATABASE_URL`)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

@app.route('/api')
def index():
    return "Running"

if __name__ == "__main__":
    app.run(debug=True)
