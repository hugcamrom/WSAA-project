from flask import Flask, render_template, request, jsonify
from db import db  # ✅ import from db.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# No need to import models here yet

if __name__ == '__main__':
    app.run(debug=True)
