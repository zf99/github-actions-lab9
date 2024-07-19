# tests/test_app.py
import pytest
from my_app.app import app, db, Customer, Product

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_customers(client):
    response = client.get('/customers')
    assert response.status_code == 200
    assert response.json == []

    customer = Customer(name='John Doe', email='john@example.com')
    db.session.add(customer)
    db.session.commit()

    response = client.get('/customers')
    assert response.status_code == 200
    assert response.json == [{'id': customer.id, 'name': 'John Doe', 'email': 'john@example.com'}]

def test_post_customer(client):
    response = client.post('/customers', json={'name': 'Jane Smith', 'email': 'jane@example.com'})
    assert response.status_code == 201
    assert response.json == {'message': 'Customer added'}

    customers = Customer.query.all()
    assert len(customers) == 1
    assert customers[0].name == 'Jane Smith'
    assert customers[0].email == 'jane@example.com'

def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert response.json == []

    product = Product(name='Product 1', price=9.99)
    db.session.add(product)
    db.session.commit()

    response = client.get('/products')
    assert response.status_code == 200
    assert response.json == [{'id': product.id, 'name': 'Product 1', 'price': 9.99}]

# Add more tests for other routes and functionality

if __name__ == '__main__':
    pytest.main()