# ============================================================
# OCR FASTAPI SERVICE
# ============================================================
#
# Technology:
#   FastAPI
#   OpenCV
#   Tesseract OCR
#   Pandas
#   NumPy
#
# Purpose:
#   1. Upload an image
#   2. Run OCR
#   3. Group OCR words into complete visual lines
#   4. Search requested keywords inside those lines
#   5. Return the complete matching line
#   6. Return OCR confidence and coordinates
#
# Example image text:
#
#   Jaswanth Scans
#   Invoice:- 12345
#   Amount:- 500
#   GST:- 90
#   Total Amount:- 590
#   Due Date: 30/08/2026
#
# Searching:
#
#   Invoice
#
# Returns approximately:
#
#   Invoice:- 12345
#
# ============================================================


# ============================================================
# 1. IMPORT REQUIRED LIBRARIES
# ============================================================

import logging
# logging is Python's built-in logging system.
# We use it to save application activity/errors into app.log
# and also display them in the terminal.

# re module provides regular expression operations for pattern matching in strings
# Use it to search, match, split, and replace text based on patterns, 
# validate input formats, or extract specific data from strings.
import re

import cv2
# OpenCV is used for image processing.
# We use it to:
#   - decode the uploaded image
#   - convert it to grayscale
#   - apply thresholding


import numpy as np
# NumPy is used to convert the uploaded image bytes
# into an array that OpenCV can understand.


import pandas as pd
# Pandas is used to convert Tesseract's OCR dictionary
# into a DataFrame.
#
# This makes filtering, grouping and processing OCR data
# much easier.


import pytesseract
# pytesseract is the Python wrapper for the
# Tesseract OCR engine.

from fastapi import (
    FastAPI,
    File,
    Form,
    UploadFile,
    HTTPException
)
# FastAPI       -> Creates our REST API
# File          -> Receives uploaded files
# Form          -> Receives form-data fields
# UploadFile    -> Represents the uploaded image
# HTTPException -> Returns proper HTTP error responses


# ============================================================
# 2. TESSERACT CONFIGURATION
# ============================================================

# Tell pytesseract exactly where Tesseract OCR
# is installed on Windows.
#
# IMPORTANT:
# Make sure this path actually exists on your computer.

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# ============================================================
# 3. LOGGING CONFIGURATION
# ============================================================

# Name of the application log file.
LOG_FILE = "app.log"


# Configure the logging system.
logging.basicConfig(

    # Record INFO, WARNING and ERROR messages.
    level=logging.INFO,

    # Format of every log message.
    #
    # Example:
    #
    # 2026-08-20 18:30:10 - INFO - OCR started
    format="%(asctime)s - %(levelname)s - %(message)s",

    handlers=[

        # Save logs into app.log.
        logging.FileHandler(
            LOG_FILE,
            encoding="utf-8"
        ),

        # Also display logs in the terminal.
        logging.StreamHandler()
    ]
)


# Create a dedicated logger for this application.
logger = logging.getLogger("ocr-logger")


# ============================================================
# 4. CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(

    # Application name shown in Swagger UI.
    title="Dynamic OCR Text Extractor",

    # Description shown in Swagger UI.
    description=(
        "Upload an image and provide keywords "
        "to extract complete matching OCR lines "
        "with confidence and coordinates."
    ),

    # API version.
    version="2.0.0"
)


# ============================================================
# 5. HEALTH CHECK API
# ============================================================

@app.get("/")
async def health_check():

    # Write a message to the application log.
    logger.info(
        "Health Check API is running successfully"
    )

    # Return a JSON response.
    return {
        "status": "ok",
        "message": "FastAPI-OCR API is running"
    }

# ============================================================
# STORE LATEST OCR RESPONSE
# ============================================================

# This variable temporarily stores the most recent OCR result.
#
# IMPORTANT:
# This is in-memory storage.
#
# It will be lost when:
# - the application restarts
# - Uvicorn reloads
# - the process crashes
#
# This is suitable for local development/testing only.

latest_ocr_response = None


# ============================================================
# GET ROUTE - VIEW LATEST OCR RESPONSE
# ============================================================

@app.get(
    "/ocr-result/",
    tags=["OCR Result"]
)
async def get_latest_ocr_result():

    # Check whether an OCR request has been processed yet.

    if latest_ocr_response is None:

        return {
            "status": "No OCR result available",
            "message": (
                "Upload an image using the POST "
                "/extract-custom-words/ endpoint first."
            ),
            "data": []
        }


    # Return the most recently generated OCR response.

    return latest_ocr_response

# ============================================================
# 6. OCR API
# ============================================================

@app.post(
    "/extract-custom-words/",
    tags=["OCR Processing"]
)
async def extract_custom_words(

    # --------------------------------------------------------
    # IMAGE FILE
    # --------------------------------------------------------
    #
    # Example:
    #
    # Screenshot.png
    #
    # UploadFile allows FastAPI to receive the image
    # through multipart/form-data.

    file: UploadFile = File(
        ...,
        description=(
            "Upload PNG, JPG, JPEG, TIFF or BMP image"
        )
    ),


    # --------------------------------------------------------
    # SEARCH KEYWORDS
    # --------------------------------------------------------
    #
    # Example:
    #
    # Invoice
    #
    # or:
    #
    # Invoice,GST,Total Amount
    #
    # The user supplies these through form-data.

    search_keywords: str = Form(
        ...,
        description=(
            "Words or phrases to search for, "
            "separated by commas. "
            "Example: Invoice, GST, Total Amount"
        )
    ),

    # --------------------------------------------------------
    # MINIMUM OCR CONFIDENCE
    # --------------------------------------------------------
    #
    # Default:
    #
    # 75%
    #
    # OCR results below this value will be removed
    # before keyword matching.

    min_confidence: float = Form(
        90.0,
        description=(
            "Minimum OCR confidence threshold "
            "from 0 to 100"
        )
    )
):

    try:

        # ====================================================
        # 7. VALIDATE FILE NAME
        # ====================================================

        # Make sure the uploaded file has a filename.
        if not file.filename:

            raise HTTPException(
                status_code=400,
                detail="No filename was provided."
            )


        # Convert the filename to lowercase.
        # This allows:
        #
        # IMAGE.JPG
        # image.jpg
        #
        # to be treated the same way.

        filename = file.filename.lower()


        # ====================================================
        # 8. ALLOWED IMAGE EXTENSIONS
        # ====================================================

        # Define supported image formats.

        allowed_extensions = (
            ".png",
            ".jpg",
            ".jpeg",
            ".tiff",
            ".bmp"
        )


        # Reject unsupported files.

        if not filename.endswith(
            allowed_extensions
        ):

            raise HTTPException(
                status_code=400,
                detail=(
                    "Unsupported image format. "
                    "Upload PNG, JPG, JPEG, TIFF or BMP."
                )
            )


        # ====================================================
        # 9. VALIDATE CONFIDENCE
        # ====================================================

        # Confidence must be between 0 and 100.

        if not 0 <= min_confidence <= 100:

            raise HTTPException(
                status_code=400,
                detail=(
                    "min_confidence must be "
                    "between 0 and 100."
                )
            )


        # ====================================================
        # 10. VALIDATE SEARCH KEYWORDS
        # ====================================================

        # Remove spaces from the beginning and end.

        search_keywords = search_keywords.strip()


        # Reject empty keyword input.

        if not search_keywords:

            raise HTTPException(
                status_code=400,
                detail=(
                    "At least one search keyword "
                    "is required."
                )
            )


        # ====================================================
        # 11. READ UPLOADED IMAGE
        # ====================================================

        # Read the uploaded image as raw bytes.

        contents = await file.read()


        # Convert raw bytes into a NumPy array.

        nparr = np.frombuffer(
            contents,
            np.uint8
        )


        # ====================================================
        # 12. DECODE IMAGE USING OPENCV
        # ====================================================

        # Convert the NumPy byte array into an OpenCV image.

        img = cv2.imdecode(
            nparr,
            cv2.IMREAD_COLOR
        )

        """
        # Debugging - Save the original image for debugging #

        cv2.imwrite("debug_original.png", img)

        # Test 1: Original image

        print("\n===== ORIGINAL =====")

        print(
            pytesseract.image_to_string(
                img,
                config=r"--oem 3 --psm 6"
            )
        )   
        """

        # If OpenCV cannot decode the image,
        # the uploaded file is probably invalid/corrupt.

        if img is None:

            raise HTTPException(
                status_code=400,
                detail=(
                    "Failed to decode image data."
                )
            )


        # Log successful image upload.

        logger.info(
            "Image uploaded successfully: %s",
            file.filename
        )

        # ====================================================
        # 13. CONVERT IMAGE TO GRAYSCALE - IMAGE PREPROCESSING FOR OCR
        # ====================================================

        # Original image:
        #
        # BGR / Color
        #
        # OCR usually doesn't need color.
        #
        # Convert the original color image into grayscale.

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        """
        # Debugging - Save grayscale image for debugging #

        cv2.imwrite("debug_gray.png", gray)

        # Test 2: Grayscale image
        print("\n===== GRAYSCALE =====")

        print(
            pytesseract.image_to_string(
                gray,
                config=r"--oem 3 --psm 6"
            )
        )
        """

        # ------------------------------------------------------------
        # 14. UPSCALE IMAGE
        # ------------------------------------------------------------
        #
        # Your uploaded image is relatively small.
        #
        # Increasing its size gives Tesseract more pixels to work with
        # when recognizing small characters and numbers.
        #
        # 4x works well for this particular type of screenshot.

        scale_factor = 4

        upscaled = cv2.resize(
            gray,
            None,
            fx = scale_factor,
            fy = scale_factor,
            interpolation = cv2.INTER_CUBIC
        )

        """
        # Debugging - Save upscaled image for debugging #

        cv2.imwrite("debug_upscaled.png", upscaled)

        # Test 3: Upscaled image
        print("\n===== UPSCALED =====")

        print(
            pytesseract.image_to_string(
                upscaled,
                config=r"--oem 3 --psm 6"
            )
        )
        """

        """
        # ====================================================
        # 15. APPLY OTSU THRESHOLDING
        # ====================================================

        # Convert grayscale image into a binary
        # black-and-white image.
        #
        # OTSU automatically calculates a suitable
        # threshold value.

        _, thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU
        )
        """

        """
        # Debugging - Save final threshold image that will be sent to Tesseract #

        cv2.imwrite("debug_threshold.png", thresh)

        # Test 4: Threshold image
        print("\n===== THRESHOLD =====")

        print(
            pytesseract.image_to_string(
                thresh,
                config=r"--oem 3 --psm 6"
            )
        )
        """

        # ====================================================
        # 16. TESSERACT CONFIGURATION
        # ====================================================

        # OEM 3:
        # Let Tesseract automatically select the OCR engine.
        #
        # PSM 6:
        # Sparse text mode.
        #
        # This works reasonably well for text that is
        # separated into different lines/areas.

        custom_config = (
            r"--oem 3 --psm 6"
        )

        """
        # test different PSM values

        for config in custom_config:

            print("\n==============================")
            print("CONFIG:", config)
            print("==============================")

            text = pytesseract.image_to_string(
                upscaled,
                config=custom_config
            )

            print(text)
        """

        # ====================================================
        # 17. RUN TESSERACT OCR
        # ====================================================

        # image_to_data() is important here.
        #
        # We don't use image_to_string() because we need:
        #
        #   text
        #   confidence
        #   left
        #   top
        #   width
        #   height
        #   block_num
        #   par_num
        #   line_num
        #
        # The last three are especially important because
        # they allow us to reconstruct complete visual lines.

        ocr_data = pytesseract.image_to_data(
            upscaled,
            config=custom_config,
            output_type=pytesseract.Output.DICT
        )

        """
        # Debugging - Raw Tesseract output #
        # temproarily print for testing

        for i in range(len(ocr_data["text"])):

            text = ocr_data["text"][i]

            if text.strip():

                print(
                    "TEXT:",
                    repr(text),
                    "| CONF:",
                    ocr_data["conf"][i],
                    "| LEFT:",
                    ocr_data["left"][i],
                    "| TOP:",
                    ocr_data["top"][i],
                    "| LINE:",
                    ocr_data["line_num"][i]
                )
        """     

        # ====================================================
        # 18. CONVERT OCR DATA TO PANDAS DATAFRAME
        # ====================================================

        # Tesseract returns a dictionary.
        #
        # Pandas converts it into a table like:
        #
        # text       conf   left   top   width   height
        # ------------------------------------------------
        # Invoice:- 91     24     49    70      16
        # 12345      96     100    49    50      16
        #
        # This is much easier to process with Pandas.

        df = pd.DataFrame(
            ocr_data
        )

        """
        # Debugging - Dataframe #

        print(
            df[
                [
                    "text",
                    "conf",
                    "left",
                    "top",
                    "width",
                    "height",
                    "block_num",
                    "par_num",
                    "line_num"
                ]
            ].to_string(index=False)
        )
        """

        # ====================================================
        # 18. CHECK REQUIRED COLUMNS
        # ====================================================

        # These columns are required for our application.
        #
        # IMPORTANT:
        #
        # block_num
        # par_num
        # line_num
        #
        # are now included because we use them to combine
        # OCR words belonging to the same visual line.

        required_cols = [

            "text",

            "conf",

            "left",

            "top",

            "width",

            "height",

            "block_num",

            "par_num",

            "line_num"
        ]


        # Make sure every required column exists.

        if not all(
            col in df.columns
            for col in required_cols
        ):

            return {

                "status": "Success",

                "uploaded_file": file.filename,

                "keywords_searched": [
                    word.strip()
                    for word in search_keywords.split(",")
                    if word.strip()
                ],

                "total_matches_found": 0,

                "message": (
                    "No readable structural "
                    "layout found in image."
                ),

                "data": []
            }


        # ====================================================
        # 19. CLEAN OCR TEXT
        # ====================================================

        # Convert every OCR result into a string.

        df["text"] = (
            df["text"]
            .astype(str)
            .str.strip()
        )


        # ====================================================
        # 20. CLEAN OCR CONFIDENCE
        # ====================================================

        # Tesseract confidence values need to be numeric.
        #
        # If conversion fails:
        #
        # errors="coerce"
        #
        # converts invalid values to NaN.
        #
        # fillna(0.0)
        #
        # converts NaN to 0.

        df["conf"] = (
            pd.to_numeric(
                df["conf"],
                errors="coerce"
            )
            .fillna(0.0)
            .astype(float)
        )


        # ====================================================
        # 21. REMOVE EMPTY OCR RESULTS
        # ====================================================

        # Tesseract can return rows where text is empty.
        #
        # We don't need those rows.

        df = df[
            df["text"] != ""
        ]


        # ====================================================
        # 22. REMOVE ONLY EMPTY OCR TOKENS
        # ============================================================

        # Keep every OCR token at this stage.
        # IMPORTANT:
        # Do NOT remove low-confidence tokens yet.
        
        # A low-confidence token may still be an important part
        # of a complete line.
        
        # Example:
        # Amount:  -> 64%
        # 500      -> 90%
        # We need BOTH tokens to reconstruct:
        # Amount: - 500

        df = df[
            df["text"] !=""
        ]

        # ====================================================
        # 23. GROUP OCR WORDS BY VISUAL LINE
        # ====================================================

        # This is the MAIN CHANGE for your new requirement.
        
        # Tesseract gives every OCR token:
  
        # block_num
        # par_num
        # line_num
     
        # Example:
        
        # Invoice:- -> block 1, paragraph 1, line 1
        # 12345     -> block 1, paragraph 1, line 1
        
        # Therefore both belong to the same visual line.
        
        # Pandas groupby() combines them.
        
        line_groups = df.groupby(
            [
                "block_num",
                "par_num",
                "line_num"
            ]
        )

        # ====================================================
        # 23. PREPARE SEARCH KEYWORDS
        # ====================================================

        # Example input:
        #
        # Invoice,GST,Total Amount
        #
        # becomes:
        #
        # ["invoice", "gst", "total amount"]
        #
        # lower() makes the search case-insensitive.

        search_targets = [
            word.strip().lower()
            for word in search_keywords.split(",")
            if word.strip()
        ]

        # ====================================================
        # 25. CREATE MATCH RESULT LIST
        # ====================================================

        # Every matching OCR line will be stored here.

        matches = []


        # ====================================================
        # 26. PROCESS EACH OCR LINE
        # ====================================================

        for _, line_df in line_groups:

            # ------------------------------------------------
            # SORT WORDS FROM LEFT TO RIGHT
            # ------------------------------------------------
            #
            # Tesseract normally returns words in order,
            # but explicitly sorting by "left" makes sure
            # our reconstructed line follows the visual order.

            line_df = line_df.sort_values(
                by="left"
            )


            # ------------------------------------------------
            # COMBINE ALL WORDS IN THE LINE
            # ------------------------------------------------
            #
            # Example:
            #
            # Tesseract:
            #
            # Invoice:-
            # 12345
            #
            # becomes:
            #
            # Invoice:- 12345

            line_text = " ".join(
                line_df["text"].astype(str)
            )

            line_text = re.sub(
                r"\s*:s*",
                ":- ",
                line_text
            )

            line_text = re.sub(
                r":-\s",
                ":- ",
                line_text
            )

            line_text = re.sub(
                r"\s+",
                "",
                line_text
            ).strip()

            # Create a lowercase version for keyword searching.
            #
            # Example:
            #
            # Invoice:- 12345
            #
            # becomes:
            #
            # invoice:- 12345

            searchable_line = line_text.lower()

            # ------------------------------------------------
            # CHECK EVERY SEARCH KEYWORD
            # ------------------------------------------------

            for search_target in search_targets:

                # Check whether the requested keyword/phrase
                # exists anywhere inside the complete OCR line.
                #
                # Example:
                #
                # search_target:
                # invoice
                #
                # searchable_line:
                # invoice:- 12345
                #
                # Result:
                # True

                if search_target not in searchable_line:

                    # Keyword wasn't found in this line.
                    # Continue checking the next keyword/line.

                    continue


                # ============================================
                # 27. CALCULATE LINE CONFIDENCE
                # ============================================

                # A line can contain multiple OCR tokens.
                #
                # Example:
                #
                # Invoice:- -> 91%
                # 12345     -> 96%
                #
                # We calculate the average:
                #
                # (91 + 96) / 2 = 93.5%
                #
                # This represents the average OCR confidence
                # of the complete line.

                line_confidence = (
                    line_df["conf"].mean()
                )


                # ============================================
                # 28. CALCULATE LINE LEFT COORDINATE
                # ============================================

                # Find the left-most OCR token.

                x_left = int(
                    line_df["left"].min()
                )

                # ============================================
                # 29. CALCULATE LINE TOP COORDINATE
                # ============================================

                # Find the top-most OCR token.

                y_top = int(
                    line_df["top"].min()
                )


                # ============================================
                # 30. CALCULATE RIGHT EDGE
                # ============================================

                # For every OCR token:
                #
                # right edge = left + width
                #
                # Find the maximum right edge.

                x_right = int(
                    (
                        line_df["left"]
                        + line_df["width"]
                    ).max()
                )

                # ============================================
                # 31. CALCULATE BOTTOM EDGE
                # ============================================

                # For every OCR token:
                #
                # bottom edge = top + height
                #
                # Find the maximum bottom edge.

                y_bottom = int(
                    (
                        line_df["top"]
                        + line_df["height"]
                    ).max()
                )

                # ============================================
                # 32. CALCULATE COMPLETE LINE WIDTH
                # ============================================

                # Example:
                #
                # x_left  = 24
                # x_right = 160
                #
                # width = 160 - 24
                #
                # This bounding box covers the entire line.

                total_width = (
                    x_right - x_left
                )

                # ============================================
                # 33. CALCULATE COMPLETE LINE HEIGHT
                # ============================================

                total_height = (
                    y_bottom - y_top
                )

                # ============================================
                # 34. ADD MATCH TO RESULT - EXTRACT FIELD AND VALUE FROM OCR LINE
                # ============================================
                # Example OCR line:
                #
                # "Invoice:- 12345"
                #
                # We want:
                #
                # field = "Invoice"
                # value = "12345"

                field = search_target.strip()

                # Remove the searched keyword from the beginning
                # of the OCR line.
                #
                # Example:
                #
                # "Invoice:- 12345"
                #        ↓
                # ":- 12345"

                remaining_text = line_text.strip()

                remaining_text = remaining_text[
                    len(field):
                ].strip()


                # Remove separators between field and value.
                #
                # Examples:
                #
                # ":- 12345"
                # ": 12345"
                # "- 12345"
                #
                # becomes:
                #
                # "12345"

                remaining_text = remaining_text.lstrip(
                    " :-="
                ).strip()

                # ------------------------------------------------
                # ADD RESULT
                # ------------------------------------------------

                matches.append({

                    # Field name that the user searched for.
                    #
                    # Example:
                    # "Invoice"

                    "field": field,

                    # Actual value found after the field.
                    #
                    # Example:
                    # "12345"

                    "value": remaining_text,

                    # Average OCR confidence for the complete line.

                    "confidence_score": (
                        f"{line_confidence:.2f}%"
                    ),

                    # Complete line coordinates.

                    "coordinates": {

                        "x_axis_left": x_left,

                        "y_axis_top": y_top,

                        "width": total_width,

                        "height": total_height
                    }
                })
                # The current line already matched a keyword.
                #
                # We don't need to add the same line multiple
                # times if multiple search keywords overlap.

                break

        # ====================================================
        # 35. LOG OCR RESULT
        # ====================================================

        # Write the final OCR result count to app.log
        # and terminal.

        logger.info(
            "OCR completed successfully. "
            "File=%s, Matches=%s",
            file.filename,
            len(matches)
        )

        # ====================================================
        # 36. RETURN JSON RESPONSE
        # ====================================================

        response = {

            # API status.
            "status": "Success",


            # Original uploaded filename.
            "uploaded_file": file.filename,


            # Keywords supplied by the user.
            #
            # Example:
            #
            # ["Invoice", "GST", "Total Amount"]

            "keywords_searched": [
                word.strip()
                for word in search_keywords.split(",")
                if word.strip()
            ],


            # Number of matching complete lines.

            "total_matches_found": len(matches),


            # Matching OCR lines.

            "data": matches
        }

        # ============================================================
        # SAVE LATEST RESPONSE
        # ============================================================
        # Tell Python that we want to modify the global variable.
        
        global latest_ocr_response

        # Store the response so the GET endpoint can return it.

        latest_ocr_response = response

        # Return the same response to the POST request.
        
        return response

    # ========================================================
    # 37. HANDLE HTTP EXCEPTIONS
    # ========================================================

    except HTTPException:

        # If we intentionally generated an HTTP error above,
        # don't convert it into a generic 500 error.

        raise

    # ========================================================
    # 38. HANDLE UNEXPECTED ERRORS
    # ========================================================

    except Exception as e:

        # logger.exception() records the complete traceback,
        # which is extremely useful for debugging.

        logger.exception(
            "OCR Runtime Engine Error"
        )

        # Return a controlled HTTP 500 response.

        raise HTTPException(
            status_code=500,
            detail=(
                f"OCR Runtime Engine Error: {str(e)}"
            )
        )

# ============================================================
# 39. APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":

    # Import Uvicorn only when this file is executed directly.

    import uvicorn


    # Start the FastAPI development server.

    uvicorn.run(

        # Current Python file:
        # ocr-service.py
        #
        # FastAPI application object:
        # app

        "ocr-service-v2:app",

        # Only allow connections from this computer.

        host="127.0.0.1",

        # FastAPI/Uvicorn development port.

        port=8000,

        # Automatically reload the application
        # when source code changes.

        reload=True
    )