from flask import Blueprint, Flask, jsonify

# Create Flask application
app = Flask(__name__)

# Create a Flask Blueprint for the items API
items_bp = Blueprint('items', __name__)

# Sample items data
items = {
    1: {
        "id": 1,
        "name": "Laptop",
        "price": 50000
    },
    2: {
        "id": 2,
        "name": "Mobile",
        "price": 20000
    },
    3: {
        "id": 3,
        "name": "Keyboard",
        "price": 1500
    }
}

@items_bp.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask App!"

# GET /items/1
@items_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):

    # Find item using ID
    item = items.get(item_id)

    # Check whether item exists
    if not item:
        return jsonify({
            "error": "Item not found"
        }), 404

    # Return item as JSON
    return jsonify(item), 200

# IMPORTANT: Register Blueprint
app.register_blueprint(items_bp)

# Entry point
if __name__ == "__main__":
    app.run(debug=True, port=5000)