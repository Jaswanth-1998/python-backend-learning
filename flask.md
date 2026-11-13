Flask CRUD API — Line-by-Line Reference
A function-based REST/RESTful CRUD blueprint using Flask, with in-memory storage.
Use this as a template for any new Flask project's starting skeleton.
Full Code
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

items = {
    1: {"id": 1, "name": "Item One", "description": "First sample item"},
    2: {"id": 2, "name": "Item Two", "description": "Second sample item"},
}
next_id = 3


@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Flask CRUD API is running"}), 200


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(list(items.values())), 200


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


@app.route("/items", methods=["POST"])
def create_item():
    global next_id
    data = request.get_json(silent=True)

    if not data or "name" not in data:
        return jsonify({"error": "'name' field is required"}), 400

    new_item = {
        "id": next_id,
        "name": data["name"],
        "description": data.get("description", ""),
    }
    items[next_id] = new_item
    next_id += 1

    return jsonify(new_item), 201


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])

    return jsonify(item), 200


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = items.pop(item_id, None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"message": f"Item {item_id} deleted", "item": item}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
```
---
Line-by-Line Explanation
Imports & app setup
```python
from flask import Flask, request, jsonify
```
`Flask` — the class used to create the web application instance.
`request` — gives access to incoming HTTP request data (JSON body, headers, query params).
`jsonify` — converts Python dicts/lists into a proper JSON HTTP response (correct `Content-Type`, correct encoding).
```python
app = Flask(__name__)
```
Creates the application object. `__name__` tells Flask the current module's name, used internally to locate resources (templates, static files) relative to this file.
Real-world difference: Production apps usually wrap this in an app factory function (`create_app()`), not create it at module level — this lets you spin up multiple app instances (test config, prod config, dev config) cleanly.
In-memory "database"
```python
items = {
    1: {"id": 1, "name": "Item One", "description": "First sample item"},
    2: {"id": 2, "name": "Item Two", "description": "Second sample item"},
}
next_id = 3
```
`items` — a plain Python dict standing in for a database table. Key = item id, value = item data.
`next_id` — manually tracks the next id to assign.
Real-world difference: Replaced by a real database (PostgreSQL/MySQL/SQLite) via an ORM like SQLAlchemy. IDs are DB-generated (auto-increment or UUID), not tracked manually — and data survives restarts, unlike this dict.
Health check route
```python
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Flask CRUD API is running"}), 200
```
The decorator binds this function to `GET /`.
`jsonify(...)` builds the JSON body; `200` is the HTTP status code (OK).
Real-world difference: Production health checks often also ping the database to confirm it's reachable, so orchestrators (Kubernetes, load balancers) know if the app is actually healthy — not just that the process is alive.
GET all items
```python
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(list(items.values())), 200
```
`items.values()` returns all item dicts; `list(...)` converts the view to a list; `jsonify` serializes it into a JSON array.
Real-world difference: Real APIs paginate (`?page=1&limit=20`) instead of returning every row, and usually support filtering/sorting query params.
GET single item
```python
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200
```
`<int:item_id>` is a URL converter — extracts the id from the path and casts it to `int` automatically.
`dict.get()` returns `None` instead of raising `KeyError` if the key is missing.
`404` = Not Found, the standard REST code for a missing resource.
Real-world difference: `items.get(item_id)` becomes `Item.query.get(item_id)` with SQLAlchemy — same logic, querying a real table.
POST — create item
```python
@app.route("/items", methods=["POST"])
def create_item():
    global next_id
    data = request.get_json(silent=True)

    if not data or "name" not in data:
        return jsonify({"error": "'name' field is required"}), 400

    new_item = {
        "id": next_id,
        "name": data["name"],
        "description": data.get("description", ""),
    }
    items[next_id] = new_item
    next_id += 1

    return jsonify(new_item), 201
```
`global next_id` — required because we reassign `next_id` (a module-level variable) inside the function; without it Python treats `next_id += 1` as an undefined local variable and raises `UnboundLocalError`.
`request.get_json(silent=True)` — parses the JSON body; `silent=True` returns `None` instead of raising an error on malformed/missing JSON.
`"name" not in data` — manual required-field validation; `400` = Bad Request.
`new_item["id"] = next_id` — assigns a unique id so the client can reference this item later.
`items[next_id] = new_item` — actually saves the item into the store. Without this line the item is returned once but never persisted.
`next_id += 1` — bumps the counter so the next item gets a different id. Without this, every new item overwrites the previous one.
`201` = Created, the correct status code for a successful resource creation (not `200`).
Real-world difference: `global next_id` disappears — the DB generates ids. Manual `"name" not in data` checks are replaced by schema validation (Pydantic/Marshmallow), which also checks types, length, and format.
PUT — update item
```python
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])

    return jsonify(item), 200
```
`data.get("name", item["name"])` — if `"name"` is present in the request, use it; otherwise keep the existing value.
Real-world difference: This code behaves like a PATCH (partial update) but is mapped to `PUT`. Real projects distinguish them: `PUT` should require and replace all fields, `PATCH` allows partial updates. Updates also go through `db.session.commit()` instead of mutating a dict in place.
DELETE item
```python
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = items.pop(item_id, None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"message": f"Item {item_id} deleted", "item": item}), 200
```
`dict.pop(key, default)` removes and returns the value, or returns `None` (instead of raising `KeyError`) if the key doesn't exist.
Real-world difference: Many production APIs use soft deletes (`is_deleted = True` flag) instead of hard-removing rows, preserving audit history and allowing recovery.
Entry point
```python
if __name__ == "__main__":
    app.run(debug=True, port=5000)
```
Only runs the built-in dev server when this file is executed directly (not when imported elsewhere). `debug=True` enables auto-reload and detailed error pages — dev only.
Real-world difference: This block essentially never runs in production. Instead:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
A WSGI server (Gunicorn/uWSGI) runs multiple worker processes, `debug=True` is off (it's a security risk — can leak stack traces/source), and the app sits behind Nginx, often inside Docker.
---
Why Flask needs `jsonify()`
Flask is a general-purpose web framework — a route can return HTML, plain text, a rendered template, a file, or JSON. Flask has no way of knowing which you want, so you must explicitly convert dicts/lists to a proper JSON HTTP response using `jsonify()`. (Flask 2.x+ will auto-convert a plain dict return value, but `jsonify()` remains best practice since it reliably handles lists, custom types, and sets the correct headers.)
```python
return jsonify({"id": 1}), 200
```
---
Real-World Differences — Summary Table
This demo |	Real-world project
`items = {}` dict |	PostgreSQL/MySQL table via SQLAlchemy ORM
`next_id` counter + `global` |	DB auto-increment / UUID primary key
Manual `if "name" not in data` |	Pydantic/Marshmallow schema validation
`app.run(debug=True)` |	Gunicorn/uWSGI + Nginx, `debug=False`
One flat file |	Blueprints split by resource, config files, `.env`
No auth	| JWT/OAuth2 on protected routes
Hard delete	| Often soft delete (`is_deleted` flag)
`list(items.values())` (all rows) | Paginated query (`LIMIT`/`OFFSET`)
App created at module level	| App factory pattern (`create_app()`)
No API docs | Added manually via `flask-swagger`/`flasgger` (not built-in)

Quick Reference — HTTP Status Codes Used

Code | Meaning | Used in
200	| OK | GET, PUT, DELETE success
201	| Created | POST success
400	| Bad Request | Missing/invalid request body
404	| Not Found | Item doesn't exist
