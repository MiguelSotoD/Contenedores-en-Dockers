from flask import Flask, jsonify

app = Flask(__name__)

#Rutes
@app.route('/products', methods=['GET'])
def get_products():
    products =[
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mouse"},
        {"id": 3, "name": "Keyboard"}
    ]
    return jsonify(products)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)