from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

from models import Item, Category, Shop  # ✅ Move this *after* route definitions

@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    items_list = []
    for item in items:
        items_list.append({
            'id': item.id,
            'name': item.name,
            'quantity': item.quantity,
            'needed': item.needed,
            'category': item.category.name if item.category else None,
            'shop': item.shop.name if item.shop else None,
            'last_updated': item.last_updated.isoformat()
        })
    return jsonify(items_list)

if __name__ == '__main__':
    app.run(debug=True)
