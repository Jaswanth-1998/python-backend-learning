from fastapi import APIRouter, HTTPException

# Create a router for the items API
router = APIRouter()

# Sample items data
items = {
    1:{
        "id": 1,
        "name": "Laptop",
        "price": 50000
    },
    2:{
        "id": 2,
        "name": "Mobile",
        "price": 20000
    },
    3:{
        "id": 3,
        "name": "Keyboard",
        "price": 1500
    }
}
@router.get("/")
async def home():
    return {"message": "Welcome to the Items API!"}

# GET /items/1
@router.get("/items/{item_id}")
async def get_item(item_id: int):
    # Find item using ID
    item = items.get(item_id)

    # Check whether item exists
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Return item as JSON
    return item

