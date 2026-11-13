# FastAPI CRUD API — Line-by-Line Reference

A function-based REST/RESTful CRUD blueprint using FastAPI, with in-memory storage.
Use this as a template for any new FastAPI project's starting skeleton.

## Full Code

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="FastAPI CRUD Blueprint")


class Item(BaseModel):
    name: str
    description: Optional[str] = ""


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


items = {
    1: {"id": 1, "name": "Item One", "description": "First sample item"},
    2: {"id": 2, "name": "Item Two", "description": "Second sample item"},
}
next_id = 3


@app.get("/")
def health_check():
    return {"status": "ok", "message": "FastAPI CRUD API is running"}


@app.get("/items")
def get_items():
    return list(items.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    new_item = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
    }
    items[next_id] = new_item
    next_id += 1
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    existing = items.get(item_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Item not found")

    if item.name is not None:
        existing["name"] = item.name
    if item.description is not None:
        existing["description"] = item.description

    return existing


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item = items.pop(item_id, None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Item {item_id} deleted", "item": item}
```

Run with:
```bash
uvicorn fastapi-app:app --reload --port 8000
```
Auto docs: `http://127.0.0.1:8000/docs`

---

## Line-by-Line Explanation

### Imports & app setup

```python
from fastapi import FastAPI, HTTPException
```
- `FastAPI` — the class used to create the app instance.
- `HTTPException` — used to return proper error responses (equivalent of Flask's `jsonify({...}), 404`).

```python
from pydantic import BaseModel
```
`BaseModel` — base class for defining data schemas with automatic type validation.

```python
from typing import Optional
```
`Optional[str]` means "a `str`, or `None`" — used for fields that aren't required.

```python
app = FastAPI(title="FastAPI CRUD Blueprint")
```
Creates the app instance. `title` appears on the auto-generated `/docs` page.

**Real-world difference:** Same as Flask — production apps use an app-factory pattern, and split routes across files with `APIRouter()` instead of one flat `app` object.

### Schemas (the biggest structural difference vs. Flask)

```python
class Item(BaseModel):
    name: str
    description: Optional[str] = ""
```
- `name: str` — required field. If missing or the wrong type, FastAPI auto-rejects the request with a `422` error **before your function body runs**.
- `description: Optional[str] = ""` — optional, defaults to `""` if not sent.

```python
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
```
Both fields optional, defaulting to `None`, since an update may only change one field.

This entire block **replaces** Flask's manual `if not data or "name" not in data: return error` check — validation is declared once in the schema and reused everywhere `Item` is used as a parameter type.

**Real-world difference:** Production schemas add constraints (`Field(min_length=1, max_length=100)`), custom validators (`@validator`), and typically **separate models** for input vs. output (e.g. a `UserCreate` model with a password field vs. a `UserResponse` model that excludes it).

### In-memory database

```python
items = {
    1: {"id": 1, "name": "Item One", "description": "First sample item"},
    2: {"id": 2, "name": "Item Two", "description": "Second sample item"},
}
next_id = 3
```
Same concept as Flask — a dict standing in for a database, with a manual id counter.

**Real-world difference:** Replaced by a real database via SQLModel/SQLAlchemy; ids are DB-generated, not tracked manually.

### Health check

```python
@app.get("/")
def health_check():
    return {"status": "ok", "message": "FastAPI CRUD API is running"}
```
- `@app.get("/")` — a verb-specific decorator; FastAPI has one per HTTP method (`@app.get`, `@app.post`, `@app.put`, `@app.delete`) instead of `@app.route(..., methods=[...])`.
- No `jsonify()` call, no explicit status code — defaults to `200`, and the dict is auto-serialized to JSON. (See the dedicated section below on *why*.)

### GET all items

```python
@app.get("/items")
def get_items():
    return list(items.values())
```
Returning a list of dicts — FastAPI serializes it into a JSON array automatically, equivalent to Flask's `jsonify(list(...))` but without the explicit call.

**Real-world difference:** Same as Flask — add pagination (`skip`/`limit` query params) instead of returning everything.

### GET single item

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```
- `{item_id}` in the path is matched to the `item_id` function parameter.
- `item_id: int` does double duty: (1) FastAPI auto-converts the URL string to an `int`, and (2) if it isn't a valid int (`/items/abc`), FastAPI auto-returns a `422` error with **zero validation code written**.
- `raise HTTPException(...)` — not `return`. FastAPI's internal exception handler catches it and converts it into a proper JSON error response (`{"detail": "Item not found"}`) with the given status code.

**Compare to Flask:** Flask used `<int:item_id>` in the route string for the same type casting; FastAPI does it via the Python type hint instead. This is FastAPI's core philosophy — **type hints drive behavior**, not decorator syntax.

### POST — create item

```python
@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    new_item = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
    }
    items[next_id] = new_item
    next_id += 1
    return new_item
```
- `status_code=201` in the decorator sets the *default success* status for this whole route — no need to specify it on every return, unlike Flask's `return jsonify(new_item), 201`.
- `item: Item` — FastAPI parses the incoming JSON body, validates it against the `Item` schema, and hands you a real Python object (`item.name`, `item.description` as attributes) — not a raw dict like Flask's `request.get_json()`. If validation fails, the function body never runs; FastAPI returns `422` automatically.
- `items[next_id] = new_item` / `next_id += 1` — same manual store-and-increment logic as Flask, same caveats (would need `global`, would collide without the increment).

**Biggest Flask vs FastAPI difference in the whole file.** Flask's:
```python
data = request.get_json(silent=True)
if not data or "name" not in data:
    return jsonify({"error": "'name' field is required"}), 400
```
collapses into simply:
```python
def create_item(item: Item):
```

### PUT — update item

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    existing = items.get(item_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Item not found")

    if item.name is not None:
        existing["name"] = item.name
    if item.description is not None:
        existing["description"] = item.description

    return existing
```
Two parameters: `item_id` comes from the URL path, `item` comes from the JSON body — FastAPI figures out which is which based on type hints (`int` vs. a `BaseModel` subclass). `if item.name is not None` only overwrites a field if the client actually sent a value (not the schema's default `None`).

**Real-world difference:** Same PUT-vs-PATCH issue as Flask — this is really a PATCH. Production APIs typically add a dedicated `@app.patch(...)` route for partial updates and reserve `PUT` for full replacement.

### DELETE item

```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item = items.pop(item_id, None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Item {item_id} deleted", "item": item}
```
Identical logic to Flask's `dict.pop()` trick — just no `jsonify()`, and errors raised via `HTTPException` instead of returned via `jsonify(...), 404`.

### No `if __name__ == "__main__"` block — why?

FastAPI files typically have **no** equivalent to Flask's `app.run()`. FastAPI apps are served by an external **ASGI server**, `uvicorn`:

```bash
uvicorn fastapi_app:app --reload --port 8000
```

`fastapi_app:app` means "look inside `fastapi_app.py` for a variable named `app`." Uvicorn imports and serves it — FastAPI itself never starts its own server. (You *can* add a `uvicorn.run(...)` block for convenience, but it isn't idiomatic.)

---

## Why FastAPI does NOT need `jsonify()`

**Flask** is general-purpose — a route might return HTML, plain text, a template, a file, or JSON, so Flask has no way to know your intent. You must explicitly say "convert this to JSON" via `jsonify()`.

**FastAPI** is API-first by design — every route is assumed to return structured data. So the framework **automatically serializes** whatever you return (a `dict`, a `list`, or a Pydantic model) into JSON behind the scenes, using Pydantic. That's also what powers the free `/docs` page and automatic response validation.

```python
# Flask
return jsonify({"id": 1}), 200

# FastAPI — identical JSON on the wire, but no explicit conversion call
return {"id": 1}
```

---

## Flask vs FastAPI — Side-by-Side

| Concept | Flask | FastAPI |
|---|---|---|
| JSON response | Manual `jsonify(data), 200` | Automatic — just `return data` |
| Request body validation | Manual `if "name" not in data` | Automatic via Pydantic `BaseModel` |
| Path param type casting | `<int:item_id>` in route string | `item_id: int` type hint |
| Error response | `return jsonify({...}), 404` | `raise HTTPException(status_code=404, ...)` |
| Route registration | `@app.route("/x", methods=["GET"])` | `@app.get("/x")` (verb-specific decorator) |
| Auto docs | Not built-in | Free, at `/docs` and `/redoc` |
| Dev server | Built-in (`app.run()`) | External — needs `uvicorn` |
| Async support | Limited/awkward | Native (`async def` routes) |

## Real-World Differences — Summary Table

| This demo | Real-world project |
|---|---|
| `items = {}` dict | Real DB via SQLModel/SQLAlchemy |
| `next_id` counter + `global` | DB auto-increment / UUID |
| `Item` / `ItemUpdate` schemas | Same idea + `Field()` constraints, separate input/output models |
| `uvicorn --reload` (dev) | `uvicorn` + Gunicorn workers behind Nginx, in Docker, `--reload` off |
| No auth | `Depends()` for JWT/OAuth2 on protected routes |
| Hard delete | Often soft delete (`is_deleted` flag) |
| `list(items.values())` (all rows) | Paginated query (`skip`/`limit`) |

## Quick Reference — HTTP Status Codes Used

| Code | Meaning | Used in |
|---|---|---|
| 200 | OK | GET, PUT, DELETE success |
| 201 | Created | POST success |
| 404 | Not Found | Item doesn't exist |
| 422 | Unprocessable Entity | Auto-returned by FastAPI on schema/type validation failure |

---------------------------------------------------------------------------------

# FastAPI: Local In-Memory Database vs PostgreSQL

## FastAPI: From In-Memory Storage to PostgreSQL — Real-World Database Example and Comparison
## 1. Current Local/In-Memory Version

In the simple learning version, we store data inside a Python dictionary:

```python
items = {}
next_id = 1
```

Complete example:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory database
items = {}
next_id = 1


class Item(BaseModel):
    name: str
    description: str


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id

    new_item = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
    }

    items[next_id] = new_item
    next_id += 1

    return new_item
```

### How it works

If we send:

```json
{
    "name": "Laptop",
    "description": "My new laptop"
}
```

FastAPI creates:

```python
{
    "id": 1,
    "name": "Laptop",
    "description": "My new laptop"
}
```

and stores it in:

```python
items = {
    1: {
        "id": 1,
        "name": "Laptop",
        "description": "My new laptop"
    }
}
```

The problem is that this data exists **only in the Python program's memory**.

If the server restarts:

```text
Server running
     ↓
items = {1: Laptop}
     ↓
Server stops/restarts
     ↓
items = {}
     ↓
Laptop is gone
```

This is useful for learning, testing, and very simple prototypes, but it is **not suitable as the main database for a real production application**.

---

# 2. Real-World Version: FastAPI + PostgreSQL

In a real application, PostgreSQL stores the data.

The architecture becomes:

```text
Client
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

Here, we don't create:

```python
items = {}
next_id = 1
```

because PostgreSQL stores the records and manages the IDs.

---

# 3. Install the Required Packages

For a simple example:

```bash
pip install fastapi uvicorn sqlalchemy psycopg
```

`psycopg` is the PostgreSQL driver that allows Python/SQLAlchemy to communicate with PostgreSQL.

---

# 4. Database Connection

Create `database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql+psycopg://postgres:password@localhost:5432/mydb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

The connection string:

```text
postgresql+psycopg://postgres:password@localhost:5432/mydb
```

means approximately:

```text
postgresql+psycopg
        ↓
Use PostgreSQL through the psycopg driver

postgres
        ↓
Database username

password
        ↓
Database password

localhost
        ↓
PostgreSQL is running on this machine

5432
        ↓
PostgreSQL's default port

mydb
        ↓
Database name
```

In a real application, **don't hard-code the password**. Normally you use environment variables.

---

# 5. Create the Item Model

Create `models.py`:

```python
from sqlalchemy import Column, Integer, String
from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
```

This represents a PostgreSQL table:

```text
items
-----------------------------------
id | name | description
-----------------------------------
```

The important part is:

```python
id = Column(Integer, primary_key=True)
```

PostgreSQL/SQLAlchemy handles the ID generation.

Therefore, you don't need:

```python
next_id = 1
```

or:

```python
next_id += 1
```

---

# 6. Pydantic Schema

Create `schemas.py`:

```python
from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: str
```

This is used for validating the incoming JSON.

For example:

```json
{
    "name": "Laptop",
    "description": "My new laptop"
}
```

FastAPI converts the request into an `ItemCreate` object.

---

# 7. FastAPI Application

Create `main.py`:

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, get_db, Base
from models import Item
from schemas import ItemCreate


app = FastAPI()


# Create database tables
Base.metadata.create_all(bind=engine)


@app.post("/items", status_code=201)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db)
):
    new_item = Item(
        name=item.name,
        description=item.description
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item
```

---

# 8. What Happens When We Send a POST Request?

Suppose the client sends:

```http
POST /items
```

with:

```json
{
    "name": "Laptop",
    "description": "My new laptop"
}
```

FastAPI receives it:

```text
Client
   ↓
POST /items
   ↓
FastAPI
   ↓
Pydantic validates the JSON
   ↓
ItemCreate object
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

This code:

```python
new_item = Item(
    name=item.name,
    description=item.description
)
```

creates a Python representation of the database record.

Then:

```python
db.add(new_item)
```

tells SQLAlchemy:

> I want to insert this object into the database.

Then:

```python
db.commit()
```

actually saves the change to PostgreSQL.

Then:

```python
db.refresh(new_item)
```

refreshes the Python object with the values generated by the database, such as the new `id`.

The response could be:

```json
{
    "id": 1,
    "name": "Laptop",
    "description": "My new laptop"
}
```

---

# 9. What PostgreSQL Is Doing

Conceptually, SQLAlchemy is performing something similar to:

```sql
INSERT INTO items (name, description)
VALUES ('Laptop', 'My new laptop');
```

PostgreSQL stores:

```text
items
------------------------------------------------
id | name       | description
------------------------------------------------
1  | Laptop     | My new laptop
```

If we send another request:

```json
{
    "name": "Phone",
    "description": "My new phone"
}
```

PostgreSQL becomes:

```text
items
------------------------------------------------
id | name       | description
------------------------------------------------
1  | Laptop     | My new laptop
2  | Phone      | My new phone
```

We never manually wrote:

```python
next_id = 2
```

PostgreSQL handles the ID generation.

---

# 10. Main Difference

| Local/In-Memory             | PostgreSQL                     |
| --------------------------- | ------------------------------ |
| `items = {}`                | PostgreSQL table               |
| Python stores the data      | PostgreSQL stores the data     |
| `next_id` manually managed  | Database generates IDs         |
| Data exists in RAM          | Data is persisted              |
| Restart → data lost         | Restart → data remains         |
| Good for learning/testing   | Suitable for real applications |
| No database server required | PostgreSQL server required     |

### Local version

```text
FastAPI
   ↓
Python dictionary
   ↓
RAM
```

You write:

```python
items[next_id] = new_item
next_id += 1
```

### PostgreSQL version

```text
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
   ↓
Database storage
```

You write:

```python
db.add(new_item)
db.commit()
```

---

# 11. The Most Important Concept

Your original code:

```python
items = {}
next_id = 1
```

is essentially **pretending that the Python dictionary is your database**.

When you move to PostgreSQL, you replace that responsibility:

```text
BEFORE

Python
 ├── items = {}
 ├── next_id = 1
 └── stores data


AFTER

Python/FastAPI
 └── sends data to PostgreSQL

PostgreSQL
 ├── stores data
 ├── generates IDs
 ├── handles queries
 ├── handles transactions
 └── persists data
```

So you can think of the transition like this:

```text
items[next_id] = new_item
        ↓
    PostgreSQL

next_id += 1
        ↓
    PostgreSQL

items = {}
        ↓
    PostgreSQL table
```

**In a real application, FastAPI is not the database. PostgreSQL is the database. FastAPI handles the API/business logic, while PostgreSQL handles persistent data storage.**
