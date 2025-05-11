from flask import Flask, render_template, request, jsonify
from db import db  # ✅ import from db.py
from models import Item, Category, Shop  # ✅ import your models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()

    name = data.get('name')
    quantity = data.get('quantity', 1)
    needed = data.get('needed', True)
    category_id = data.get('category_id')
    shop_id = data.get('shop_id')

    new_item = Item(
        name=name,
        quantity=quantity,
        needed=needed,
        category_id=category_id,
        shop_id=shop_id
    )

    db.session.add(new_item)
    db.session.commit()

    return jsonify({'message': 'Item added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
