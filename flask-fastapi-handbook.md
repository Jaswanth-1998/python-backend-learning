# Flask + FastAPI CRUD Handbook

A single reference to revisit whenever you start a new backend project or need to recall
how Flask and FastAPI differ. Covers the CRUD blueprint, line-by-line reasoning, common doubts
(like `jsonify()`), and how each piece changes in real-world production projects.

> See also: `flask.md` and `fastapi.md` for the full annotated code of each framework individually.

---

## 1. The Core Idea

Both apps expose the **same** resource — `/items` — with the same 4 CRUD operations mapped to
HTTP verbs. This mapping is the actual "blueprint" you reuse in every project, regardless of framework:

| Operation | HTTP Verb | Path | Purpose |
|---|---|---|---|
| Create | `POST` | `/items` | Add a new resource |
| Read (all) | `GET` | `/items` | List all resources |
| Read (one) | `GET` | `/items/{id}` | Fetch a single resource |
| Update | `PUT` | `/items/{id}` | Modify a resource |
| Delete | `DELETE` | `/items/{id}` | Remove a resource |

Plus a `GET /` health check — standard in almost every real API, used by load balancers,
uptime monitors, and container orchestrators to confirm the service is alive.

---

## 2. Flask vs FastAPI — Philosophy in One Line

- **Flask** = a minimal, unopinionated toolkit. You explicitly wire up everything (JSON conversion, validation, status codes). Maximum control, more boilerplate.
- **FastAPI** = an opinionated, API-first framework built on Python type hints. Validation, serialization, and docs are automatic, driven by the types you declare.

Neither is "better" — Flask is often preferred for flexibility/simplicity/legacy projects & HTML-serving apps; FastAPI is preferred for pure JSON APIs, async workloads, and when auto-generated docs/validation save time.

---

## 3. The `jsonify()` Doubt — Why Flask Needs It and FastAPI Doesn't

**Flask is general-purpose.** A route can return HTML, plain text, a rendered template, a file, or JSON — Flask can't guess your intent. So you must explicitly say "convert this to JSON":
```python
return jsonify({"id": 1}), 200
```
(Flask 2.x+ *will* auto-convert a plain dict, but lists/other types still need it, so `jsonify()` remains best practice for consistency.)

**FastAPI is API-first.** Every route is assumed to return structured data. Whatever you return —
a `dict`, `list`, or Pydantic model — is **automatically serialized to JSON** using Pydantic under the hood:
```python
return {"id": 1}
```
Both produce identical JSON on the wire. FastAPI is just doing the `jsonify()` step invisibly, every time — which is also what powers its free `/docs` page and automatic response validation.

---

## 4. Side-by-Side: Same Feature, Both Frameworks

### App setup

```python
# Flask
from flask import Flask, request, jsonify
app = Flask(__name__)
```
```python
# FastAPI
from fastapi import FastAPI, HTTPException
app = FastAPI(title="...")
```

### Defining a route

```python
# Flask — one decorator, verb passed as an argument
@app.route("/items", methods=["GET"])
def get_items():
    ...
```
```python
# FastAPI — verb-specific decorator
@app.get("/items")
def get_items():
    ...
```

### Path parameter with type casting

```python
# Flask — type declared in the URL rule
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    ...
```
```python
# FastAPI — type declared as a Python type hint
@app.get("/items/{item_id}")
def get_item(item_id: int):
    ...
```

### Reading & validating the request body

```python
# Flask — manual parsing and manual validation
data = request.get_json(silent=True)
if not data or "name" not in data:
    return jsonify({"error": "'name' field is required"}), 400
name = data["name"]
description = data.get("description", "")
```
```python
# FastAPI — schema does the parsing AND validation
class Item(BaseModel):
    name: str
    description: Optional[str] = ""

def create_item(item: Item):
    name = item.name
    description = item.description
```

### Returning success

```python
# Flask
return jsonify(new_item), 201
```
```python
# FastAPI
@app.post("/items", status_code=201)   # status set once, in the decorator
def create_item(item: Item):
    return new_item                      # auto-serialized
```

### Returning an error

```python
# Flask
return jsonify({"error": "Item not found"}), 404
```
```python
# FastAPI
raise HTTPException(status_code=404, detail="Item not found")
```

### Running the app

```bash
# Flask — built-in dev server
python flask-app.py
```
```bash
# FastAPI — needs an external ASGI server
uvicorn fastapi-app:app --reload --port 8000
```

---

## 5. Common Doubts Log

Running list of "why do we do this?" questions worth remembering.

### Q: Why `global next_id` inside `create_item()`?
Because the function *reassigns* `next_id` (`next_id += 1`), and `next_id` is defined outside the
function (module-level). Without `global`, Python treats it as a new local variable inside the
function and raises `UnboundLocalError` the moment it's read before being locally assigned.
Reading a global (without reassigning it) never needs `global` — only reassignment does.

### Q: Why `items[next_id] = new_item` — isn't returning the item enough?
No. `new_item` only exists inside the function's local scope. Without storing it in `items`
(the "database"), it's returned to the client once and then **lost** — a later `GET /items`
would never show it. This line is what actually persists the data.

### Q: Why `next_id += 1` — what breaks without it?
Every new item would get assigned the exact same id, and `items[next_id] = new_item` would
**overwrite** the previous item stored at that key instead of adding a new one. You'd never be
able to have more than one manually-created item at a time.

### Q: Does the code crash without these lines?
No — Flask/FastAPI won't throw an error. The API keeps responding with `200`/`201`, which is
what makes this bug dangerous: it fails **silently**. You'd only notice when testing in Postman
and seeing items disappear, get overwritten, or never show up in `GET /items`.

### Q: In real projects, do we manage IDs like this (`next_id` dict)?
No. This is a teaching/demo simplification with zero setup cost. Real projects use an actual
database (PostgreSQL/MySQL/SQLite) via an ORM (SQLAlchemy for Flask, SQLModel/SQLAlchemy for
FastAPI). The database generates ids itself (auto-increment integer or UUID), which is:
- **Persistent** — survives server restarts.
- **Safe under concurrency** — no race conditions between simultaneous requests.
- **Consistent across multiple server instances** — critical once you scale horizontally
  (multiple app instances behind a load balancer would otherwise each have their own,
  conflicting, in-memory dict).

### Q: Why does Flask return `jsonify(x), 200` but FastAPI just returns `x`?
Covered in full in Section 3 above — short version: Flask is general-purpose and doesn't assume
JSON; FastAPI is API-first and always serializes to JSON automatically.

### Q: Is `PUT` in this code really a "PUT"?
Not strictly. True REST semantics say `PUT` should require and replace the **entire** resource,
while `PATCH` allows partial updates. Both the Flask and FastAPI demo code only update fields
that are present in the request body (skipping missing ones) — that's `PATCH` behavior mapped to
a `PUT` route. Real projects usually implement both verbs distinctly.

### Q: Hard delete vs soft delete?
Both demos physically remove the item from the store (`items.pop(...)`/`dict.pop(...)`) — a
**hard delete**. Many real APIs instead flip an `is_deleted = True` flag (**soft delete**), so
the row still exists for audit trails, undo functionality, and historical reporting.

---

## 6. Real-World Production Checklist

Use this when moving a demo like this toward an actual production project.

| Area | Demo (this blueprint) | Production |
|---|---|---|
| Storage | In-memory Python dict | PostgreSQL/MySQL/SQLite via ORM (SQLAlchemy / SQLModel) |
| ID generation | Manual counter (`next_id`) | DB auto-increment or UUID |
| Validation | Manual `if` checks (Flask) / Pydantic (FastAPI, already real-world-ish) | Pydantic/Marshmallow with field constraints, custom validators |
| Error handling | Basic `if not item: 404` | Centralized exception handlers, structured error responses |
| Auth | None | JWT / OAuth2 / API keys, `Depends()` in FastAPI or `flask-login`/`flask-jwt-extended` in Flask |
| Pagination | None — returns all rows | `?page=&limit=` or `?skip=&limit=` query params |
| App structure | One flat file | Blueprints (Flask) / Routers (FastAPI), split by resource/domain |
| Config | Hardcoded | `.env` files + environment-based config classes |
| Server | Built-in dev server (`app.run()` / `uvicorn --reload`) | Gunicorn/uWSGI workers (Flask) or Uvicorn workers via Gunicorn (FastAPI), behind Nginx, often in Docker |
| Debug mode | `debug=True` | Always `False` in production (security risk — leaks stack traces) |
| Logging | `print()` / none | Structured logging (e.g. `logging` module, JSON logs, sent to a log aggregator) |
| Migrations | None (no schema) | Alembic (works with both Flask-SQLAlchemy and FastAPI/SQLModel) |
| Testing | Manual Postman clicks | Automated tests with `pytest` against a test database |
| Docs | None (Flask) / free `/docs` (FastAPI) | Flask needs `flasgger`/`flask-swagger`; FastAPI's `/docs` is usually kept as-is |
| Deletion | Hard delete | Often soft delete (`is_deleted` flag) |
| Update semantics | `PUT` behaves like `PATCH` | Proper `PUT` (full replace) vs `PATCH` (partial) split |

---

## 7. HTTP Status Code Cheat Sheet (used across both apps)

| Code | Meaning | When to use |
|---|---|---|
| 200 | OK | Successful GET, PUT, DELETE |
| 201 | Created | Successful POST (new resource created) |
| 400 | Bad Request | Client sent invalid/malformed data (Flask manual check) |
| 404 | Not Found | Requested resource doesn't exist |
| 422 | Unprocessable Entity | FastAPI's automatic response when Pydantic validation fails |
| 500 | Internal Server Error | Unhandled server-side exception |

---

## 8. Minimal Postman Testing Flow

1. **Health check** → `GET /` → confirms server is up.
2. **List** → `GET /items` → see seeded data.
3. **Get one** → `GET /items/1`.
4. **Create** → `POST /items` with JSON body `{"name": "...", "description": "..."}` → expect `201`.
5. **Update** → `PUT /items/{id}` with partial/full JSON body → expect `200`.
6. **Delete** → `DELETE /items/{id}` → expect `200`.
7. **Negative test** → `GET /items/9999` → expect `404`.

---

## 9. Next Steps to Level This Up

- [ ] Swap the in-memory dict for SQLite + SQLAlchemy (Flask) / SQLModel (FastAPI).
- [ ] Add pagination (`?page=&limit=`) to the list endpoints.
- [ ] Add auth (JWT) to protect POST/PUT/DELETE.
- [ ] Split routes into Blueprints (Flask) / Routers (FastAPI) once endpoints grow.
- [ ] Add `pytest` test suite.
- [ ] Add structured logging and centralized error handling.
- [ ] Containerize with Docker + `docker-compose` (app + database).
