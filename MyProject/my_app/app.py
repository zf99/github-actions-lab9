import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

PORT = 5000
HOST = '0.0.0.0'

app = Flask(__name__)

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Set the path for the SQLite database file in the current directory
db_path = os.path.join(current_directory, 'my_app.db')

# Configure the Flask app to use the SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)


# Define the models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))


# Define a wrapper for the database operations
class DatabaseWrapper:
    @staticmethod
    def add_and_commit(model_instance):
        db.session.add(model_instance)
        db.session.commit()

    @staticmethod
    def get_all(model_class):
        return model_class.query.all()

    @staticmethod
    def delete(model_instance):
        db.session.delete(model_instance)
        db.session.commit()

    @staticmethod
    def delete_all(model_class):
        model_class.query.delete()
        db.session.commit()


# Check if the required tables exist
def check_tables_exist():
    tableError = False
    required_tables = ['customer', 'product', 'order']
    engine = db.engine
    inspector = db.inspect(engine)
    existing_tables = inspector.get_table_names()
    for table in required_tables:
        if table not in existing_tables:
            print(f"Table '{table}' does not exist. Please restart the app to create the required tables.")
            tableError = True
    return tableError


# Define routes using the wrapper
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/customers', methods=['GET', 'POST', 'DELETE'])
def customers():
    if check_tables_exist():
        return jsonify({'message': 'Table structure errors! Look at Flask app logs.'}), 404
    if request.method == 'GET':
        all_customers = DatabaseWrapper.get_all(Customer)
        customers_data = [{'id': customer.id, 'name': customer.name, 'email': customer.email} for customer in all_customers]
        return jsonify(customers_data), 200
    elif request.method == 'POST':
        data = request.get_json()
        new_customer = Customer(name=data['name'], email=data['email'])
        DatabaseWrapper.add_and_commit(new_customer)
        return jsonify({'message': 'Customer added'}), 201
    elif request.method == 'DELETE':
        DatabaseWrapper.delete_all(Customer)
        return jsonify({'message': 'All customers deleted'}), 200


@app.route('/customers/<int:customer_id>', methods=['GET', 'DELETE'])
def customer(customer_id):
    if check_tables_exist():
        return jsonify({'message': 'Table structure errors! Look at Flask app logs.'}), 404
    if request.method == 'GET':
        customer = Customer.query.get(customer_id)
        if customer:
            customer_data = {'id': customer.id, 'name': customer.name, 'email': customer.email}
            return jsonify(customer_data), 200
        else:
            return jsonify({'message': 'Customer not found'}), 404
    elif request.method == 'DELETE':
        customer = Customer.query.get(customer_id)
        if customer:
            DatabaseWrapper.delete(customer)
            return jsonify({'message': 'Customer deleted'}), 200
        else:
            return jsonify({'message': 'Customer not found'}), 404


@app.route('/products', methods=['GET', 'POST', 'DELETE'])
def products():
    if check_tables_exist():
        return jsonify({'message': 'Table structure errors! Look at Flask app logs.'}), 404
    if request.method == 'GET':
        all_products = DatabaseWrapper.get_all(Product)
        products_data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in all_products]
        return jsonify(products_data), 200
    elif request.method == 'POST':
        data = request.get_json()
        new_product = Product(name=data['name'], price=data['price'])
        DatabaseWrapper.add_and_commit(new_product)
        return jsonify({'message': 'Product added'}), 201
    elif request.method == 'DELETE':
        DatabaseWrapper.delete_all(Product)
        return jsonify({'message': 'All products deleted'}), 200


@app.route('/products/<int:product_id>', methods=['GET', 'DELETE'])
def product(product_id):
    if check_tables_exist():
        return jsonify({'message': 'Table structure errors! Look at Flask app logs.'}), 404
    if request.method == 'GET':
        product = Product.query.get(product_id)
        if product:
            product_data = {'id': product.id, 'name': product.name, 'price': product.price}
            return jsonify(product_data), 200
        else:
            return jsonify({'message': 'Product not found'}), 404
    elif request.method == 'DELETE':
        product = Product.query.get(product_id)
        if product:
            DatabaseWrapper.delete(product)
            return jsonify({'message': 'Product deleted'}), 200
        else:
            return jsonify({'message': 'Product not found'}), 404


@app.route('/orders', methods=['GET', 'POST', 'DELETE'])
def orders():
    if check_tables_exist():
        return jsonify({'message': 'Table structure errors! Look at Flask app logs.'}), 404
    if request.method == 'GET':
        all_orders = DatabaseWrapper.get_all(Order)
        orders_data = [
            {
                'id': order.id,
                'customer_id': order.customer_id,
                'product_id': order.product_id,
                'quantity': order.quantity
            }
            for order in all_orders
        ]
        return jsonify(orders_data), 200
    elif request.method == 'POST':
        data = request.get_json()
        new_order = Order(customer_id=data['customer_id'], product_id=data['product_id'], quantity=data['quantity'])
        DatabaseWrapper.add_and_commit(new_order)
        return jsonify({'message': 'Order added'}), 201
    elif request.method == 'DELETE':
        DatabaseWrapper.delete_all(Order)
        return jsonify({'message': 'All orders deleted'}), 200


@app.route('/orders/<int:order_id>', methods=['GET', 'DELETE'])
def order(order_id):
    if check_tables_exist():
        return jsonify({'message': 'Table structure errors! Look at Flask app logs.'}), 404
    if request.method == 'GET':
        order = Order.query.get(order_id)
        if order:
            order_data = {
                'id': order.id,
                'customer_id': order.customer_id,
                'product_id': order.product_id,
                'quantity': order.quantity
            }
            return jsonify(order_data), 200
        else:
            return jsonify({'message': 'Order not found'}), 404
    elif request.method == 'DELETE':
        order = Order.query.get(order_id)
        if order:
            DatabaseWrapper.delete(order)
            return jsonify({'message': 'Order deleted'}), 200
        else:
            return jsonify({'message': 'Order not found'}), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host=HOST, port=PORT)