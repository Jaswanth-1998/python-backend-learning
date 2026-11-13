import io
import logging
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import pytesseract

# Tell Python exactly where the Windows Tesseract application is located
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Configure the Logger
LOG_FILE = "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),  # Saves to file
        logging.StreamHandler()  # Prints to terminal
    ]
)
logger = logging.getLogger("ocr-logger")

app = FastAPI(title="Jaswanth - OCR Text Extraction Service",
              version="1.0.0")

@app.get("/")
async def health_check():
    logger.info(f"Health Check Api is running successfully")

    return{"status":"ok", "message":"FastAPI-OCR Api is running"}

@app.post("/ocr/extract")
async def extract_text(file: UploadFile = File(...)):
    # Log incoming request details
    logger.info(
        f"Received OCR request. File: {file.filename}, Content-Type: {file.content_type}"
        )
    
    if not file.content_type.startswith("image/"):
        logger.warning(f"Rejected upload: {file.filename} is not a valid image type.")
        raise HTTPException(status_code=400, 
                            detail="Invalid file type. Please upload an image."
                            )
                                                                                                                                        
    try:
        image_bytes = await file.read()
        logger.info(f"Successfully read {len(image_bytes)} bytes from {file.filename}")
        
        image = Image.open(io.BytesIO(image_bytes))
        
        # Log start of heavy OCR computation
        logger.info("Starting Tesseract text extraction pipeline...")
        extracted_text = pytesseract.image_to_string(image)
        
        character_count = len(extracted_text)
        logger.info(f"OCR successful. Extracted {character_count} characters.")
        
        return {
            "filename": file.filename,
            "extracted_text": extracted_text.strip(),
            "status": "success"
        }
        
    except Exception as e:
        # Crucial for debugging: Logs the exact line number and error detail to your log file
        logger.error(f"Critical failure during OCR processing: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="OCR processing failed internally.")

if __name__ == "__main__":
    import uvicorn
    # Log application startup
    logger.info("Starting FastAPI Uvicorn Server...")
    uvicorn.run("ocr-service-v1:app", host="127.0.0.1", port=8000, reload=True)
