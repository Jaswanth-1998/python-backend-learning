# FastAPI OCR Study Handbook: Async vs Def

This handbook explains how web servers handle traffic and why choosing between `async def` and standard `def` matters for your API's performance.

---

## 🍽️ The Restaurant Analogy

Think of a web server as a restaurant kitchen handling customer orders (requests).

### 1. Flask & Standard `def` (The Traditional Kitchen)
* **How it works:** Every time a customer walks in, a dedicated waiter (thread) takes their order, walks into the kitchen, waits for the chef to cook the food, and brings it back.
* **The Problem:** If the food takes 10 minutes to cook, that waiter stands completely still doing nothing. To serve 5 customers at once, the restaurant must hire 5 separate waiters. This consumes a lot of energy and space (CPU and RAM).

### 2. FastAPI & `async def` (The Modern Smart Kitchen)
* **How it works:** One single, fast waiter (the Event Loop) takes an order. If the food requires waiting (like an API call or database search), the waiter tells the kitchen "let me know when it is ready," and instantly moves to the next table to serve another customer.
* **The Advantage:** A single waiter can serve dozens of tables simultaneously without any idle waiting time.

---

## 🏎️ When to use `async def` vs `def` in FastAPI

FastAPI is highly unique because it allows you to use both types of functions. It chooses how to run your code based on how you define the endpoint.

### 🟢 Scenario A: Use `async def` (For Network Waiting)
Use this when your code spends time waiting for external systems over the internet.
* **Examples:** Fetching data from another URL, querying a modern async database, or sending an email.
* **What FastAPI does:** It runs the code directly on the main event loop. While it waits for the network response, it pauses that function and helps other users.

### 🟡 Scenario B: Use standard `def` (For Heavy Computing / CPU Tasks)
Use this when your code is performing heavy mathematical work or using traditional blocking libraries.
* **Examples:** **Pytesseract OCR processing**, resizing images, training a machine learning model, or standard file writing.
* **What FastAPI does:** FastAPI is smart! It knows heavy tasks will freeze the main event loop. Therefore, it automatically pushes standard `def` functions onto a separate background thread pool. This keeps your main server completely free to receive new incoming traffic.

---

## 🚨 Conclusion for Our OCR Project

Because **Tesseract OCR** uses intensive CPU power to scan pixels and convert them to characters, it is a **blocking operation**. 

For this specific project, defining our endpoint as a standard **`def extract_text()`** is the most professional choice. It prevents the OCR heavy-lifting from locking up the server for other users.
