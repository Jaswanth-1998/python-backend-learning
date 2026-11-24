python -m uvicorn main:app --reload --port 8000
 
Test these URLs:

URL	Expected result
http://127.0.0.1:8000/profile	Profile HTML
http://127.0.0.1:8000/items/1	Laptop JSON
http://127.0.0.1:8000/items/2	Mobile JSON
http://127.0.0.1:8000/items/999	404 JSON

