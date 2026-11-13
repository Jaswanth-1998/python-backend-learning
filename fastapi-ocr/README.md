# FastAPI OCR Text Extraction Service

A lightweight, professional backend API built with **FastAPI** and **Tesseract OCR** to extract text from images in real-time. It processes uploaded images entirely in memory for maximum speed and security, without saving temporary files to your disk.

## 🚀 Features
* **In-Memory Processing:** Images are parsed instantly via RAM bytes.
* **Professional Logging:** Automatically records server events, traffic, and errors into an `app.log` file.
* **Interactive UI:** Built-in Swagger documentation to test image uploads easily.

## 🛠️ Prerequisites
Before running the project, you must install the **Tesseract OCR engine** on your operating system:
* **Windows:** Download and run the installer from GitHub.
* **Mac:** Run `brew install tesseract`
* **Linux:** Run `sudo apt install tesseract-ocr`

## ⚙️ Installation & Setup

1. **Navigate to the project folder:**
   ```bash
   cd fastapi-ocr
   ```

2. **Install the dependencies:**
   Make sure your virtual environment (`.venv`) is activated.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the local server:**
   ```bash
   python main.py
   ```

## 🧪 Testing the API
1. Open your web browser and go to: `http://127.0.0`
2. Open the **`POST /ocr/extract`** endpoint.
3. Click **Try it out**, upload an image file containing text, and click **Execute**.
