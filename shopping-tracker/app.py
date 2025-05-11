from flask import Flask, render_template, request, jsonify
from db import db  # ok import from db.py
from models import Item, Category, Shop  # ok import your models

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
            'last_updated': item.last_updated.isoformat() if item.last_updated else None
        })
    return jsonify(items_list)


@app.route('/api/setup', methods=['POST'])
def setup_defaults():
    # Default categories
    categories = ['Food', 'Cleaning', 'Toiletries', 'Snacks']
    for name in categories:
        existing = Category.query.filter_by(name=name).first()
        if not existing:
            db.session.add(Category(name=name))

    # Default shops
    shops = [('Tesco', 'Dublin 8'), ('Lidl', 'Dublin 6'), ('SuperValu', 'Online')]
    for name, location in shops:
        existing = Shop.query.filter_by(name=name).first()
        if not existing:
            db.session.add(Shop(name=name, location=location))

    db.session.commit()
    return jsonify({'message': 'Default categories and shops added'})

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json()

    item.name = data.get('name', item.name)
    item.quantity = data.get('quantity', item.quantity)
    item.needed = data.get('needed', item.needed)
    item.category_id = data.get('category_id', item.category_id)
    item.shop_id = data.get('shop_id', item.shop_id)

    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})

@app.route('/items')
def items_page():
    return render_template('items.html')

@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in categories])

@app.route('/api/shops', methods=['GET'])
def get_shops():
    shops = Shop.query.all()
    return jsonify([{'id': s.id, 'name': s.name} for s in shops])



if __name__ == '__main__':
    app.run(debug=True)
