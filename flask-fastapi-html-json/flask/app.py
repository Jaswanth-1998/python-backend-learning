
from flask import Flask, render_template

"""
# Import items blueprint
from api.items import items_bp
"""

# Create Flask application
app = Flask(__name__)

"""
# Register API blueprint
app.register_blueprint(items_bp)
"""

# Sample user data
user = {
    "username": "Jaswanth S",
    "email": "jaswanth@example.com"
}

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask App!"

# Profile HTML route
@app.route("/profile", methods=["GET"])
def profile():

    return render_template(
        "profile.html",
        user=user
    )


# Run application
if __name__ == "__main__":
    app.run(debug=True, port=5000)
