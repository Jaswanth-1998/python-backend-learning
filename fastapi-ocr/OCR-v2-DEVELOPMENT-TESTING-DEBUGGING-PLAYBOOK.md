# Software Development, Testing & Debugging Playbook: A Practical Engineering Mindset

# OCR Project — Development, Testing & Debugging Mental Strength Guide

Based on the way we worked through your OCR project—from the first FastAPI code, errors, response design, preprocessing, Tesseract debugging, Pandas inspection, line grouping, keyword matching, and finally the folder architecture—there is a much bigger lesson:

> **The goal is not just to make this OCR project work. The goal is to learn a repeatable way to build and debug any software project.**

---

# 1. The most important mental model

Whenever you build something, don't think:

> "I need to write the code."

Think:

> **"I need to move data from input → processing → output, and I need to know where the data can become wrong."**

For your OCR project:

```text
IMAGE
  ↓
PREPROCESSING
  ↓
TESSERACT
  ↓
RAW OCR DATA
  ↓
PANDAS
  ↓
LINE GROUPING
  ↓
TEXT NORMALIZATION
  ↓
KEYWORD MATCHING
  ↓
VALUE EXTRACTION
  ↓
JSON RESPONSE
  ↓
GET RESULT
```

Every arrow is a potential failure point.

That is the fundamental debugging mindset.

---

# 2. Before starting ANY project

Use these five questions.

### 1. What am I building?

Example:

> Upload an invoice image, search for specified fields, extract their values and coordinates, and return the result through an API.

### 2. What is the input?

```text
Image
Keywords
Confidence threshold
```

### 3. What happens to the input?

```text
Image
 ↓
Decode
 ↓
Preprocess
 ↓
OCR
 ↓
Process OCR data
 ↓
Find keywords
 ↓
Extract values
```

### 4. What should the output look like?

Define this **before** writing all the logic.

```json
{
  "status": "Success",
  "uploaded_file": "invoice.png",
  "keywords_searched": [
    "Invoice",
    "GST",
    "Amount"
  ],
  "data": [
    {
      "field": "Invoice",
      "value": "12345"
    },
    {
      "field": "GST",
      "value": "90"
    },
    {
      "field": "Amount",
      "value": "500"
    }
  ]
}
```

### 5. How will I know it works?

Create test cases.

```text
Invoice → 12345
GST     → 90
Amount  → 500
```

Also test:

```text
Invalid image
Unsupported extension
Unknown keyword
Multiple keywords
No OCR result
Low confidence OCR
```

---

# 3. Don't build the whole project immediately

This is one of the biggest mistakes developers make.

Bad approach:

```text
Create 20 files
      ↓
Write everything
      ↓
Run application
      ↓
50 errors
      ↓
"I don't know where the problem is."
```

Better:

```text
Small requirement
      ↓
Small implementation
      ↓
Run
      ↓
Test
      ↓
Confirm
      ↓
Next feature
```

For OCR:

```text
1. Read image
2. Run Tesseract
3. Print text
4. Add coordinates
5. Add keyword matching
6. Add line grouping
7. Add value extraction
8. Add API
9. Add GET result
10. Refactor
```

---

# 4. Single-file development is completely valid

For your current OCR project, starting with one file was actually useful.

Something like:

```text
ocr-service-2.py
```

containing:

```text
Imports
 ↓
Tesseract configuration
 ↓
Logging
 ↓
FastAPI
 ↓
GET /
 ↓
POST /extract-custom-words/
 ↓
Image preprocessing
 ↓
Tesseract
 ↓
Pandas
 ↓
Line grouping
 ↓
Keyword matching
 ↓
Response
```

This makes learning and debugging easier because everything is visible.

### Don't prematurely create:

```text
controllers/
services/
utils/
models/
schemas/
middleware/
repositories/
```

before you even know whether the OCR algorithm works.

---

# 5. When should you create folders?

Once the single-file version works and you understand the logic, refactor it.

Your final structure can be:

```text
ocr-service/
│
├── app/
│   └── main.py
│
├── config/
│   └── settings.py
│
├── routes/
│   └── ocr_routes.py
│
├── controllers/
│   └── ocr_controller.py
│
├── services/
│   └── ocr_service.py
│
├── utils/
│   ├── image_helper.py
│   ├── ocr_helper.py
│   └── text_helper.py
│
├── debug/
│
├── uploads/
│
├── requirements.txt
├── .env
└── README.md
```

For your current **stateless OCR project**, you're right that you don't need:

```text
models/
schemas/
middleware/auth/
```

unless the requirements change.

---

# 6. What each folder actually does

Don't memorize folder names. Understand their responsibilities.

### `app/`

Application startup.

```text
Create FastAPI
Register routes
Start application
```

---

### `config/`

Configuration.

For example:

```text
Tesseract path
OCR settings
logging configuration
```

---

### `routes/`

URL definitions.

```text
POST /extract-custom-words/
GET  /ocr-result/
GET  /
```

Route's job:

> "Which endpoint was called?"

---

### `controllers/`

Request coordination.

Controller's job:

> "What should happen for this request?"

---

### `services/`

Business logic.

For your project:

```text
ocr_service.py
```

This is where the main OCR processing belongs.

---

### `utils/`

Small reusable helpers.

For example:

```text
image_helper.py
    resize_image()
    grayscale_image()

ocr_helper.py
    run_tesseract()

text_helper.py
    normalize_text()
    extract_field_value()
```

---

# 7. Your architecture applies to the whole project

You previously asked whether:

> "The correct architecture for OCR"

was only for the POST API.

No.

It describes the **whole application**.

```text
Client
   ↓
Route
   ↓
Controller
   ↓
Service
   ↓
Utils / OCR
   ↓
Result
```

POST:

```text
POST
 ↓
Route
 ↓
Controller
 ↓
OCR Service
 ↓
Preprocessing
 ↓
Tesseract
 ↓
Line processing
 ↓
Keyword matching
 ↓
Value extraction
 ↓
Result
```

GET:

```text
GET
 ↓
Route
 ↓
Controller
 ↓
Get latest result
 ↓
Return result
```

GET should **not perform OCR again**.

---

# 8. The biggest debugging lesson from your OCR project

Your original problem was:

```text
Image visibly contains:

Amount:- 500
GST:- 90
Total Amount:- 590
```

But your application eventually returned things like:

```text
Amount:- 566
GST:- 98
Total Amount:- 598
```

The wrong reaction would be:

> "My JSON logic is wrong."

Instead, we investigated the pipeline.

---

# 9. Debugging means finding the FIRST wrong result

This is probably the most important lesson I want you to keep.

Suppose:

```text
Expected:
500

Actual:
566
```

Don't immediately change the final JSON.

Ask:

> **At what stage did `500` become `566`?**

For example:

```text
Image
 ↓
500                 ✅
 ↓
Preprocessing
 ↓
500                 ✅
 ↓
Tesseract
 ↓
566                 ❌
 ↓
Pandas
 ↓
566                 ❌
 ↓
Final JSON
 ↓
566                 ❌
```

The bug is not necessarily at the final stage.

The **first incorrect stage** is Tesseract.

That's where you investigate.

---

# 10. Your preprocessing debugging was exactly the right method

We saved different stages:

```text
original
gray
upscaled
threshold
```

Then gave each to Tesseract.

You got:

```text
ORIGINAL

Amount: - 500
GST:- 98
Total Amount:- 590
```

```text
GRAYSCALE

Amount: - 500
GST:- 98
Total Amount:- 590
```

```text
UPSCALED

Amount: - 500
GST:- 90
Total Amount:- 590
```

```text
THRESHOLD

Amount: - 566
GST:- 98
Total Amount:- 598
```

Now we have evidence.

The conclusion isn't:

> "Thresholding is always bad."

The correct conclusion is:

> **"For this image, thresholding made OCR worse, while upscaling improved recognition."**

That distinction matters.

---

# 11. Never trust a common technique blindly

You might read:

> "OCR should use thresholding."

That's not enough.

Software engineering is not:

```text
Popular technique
     ↓
Automatically correct
```

Instead:

```text
Technique
 ↓
Test
 ↓
Measure
 ↓
Keep or reject
```

Your experiment showed:

```text
Upscaling → better
Thresholding → worse
```

Therefore your current baseline should use:

```text
Grayscale
 ↓
Upscaling
 ↓
Tesseract
```

rather than blindly applying Otsu thresholding.

---

# 12. Print intermediate results

When debugging normal data:

```python
print("RAW OCR:")
print(ocr_data)
```

Then:

```python
print("DATAFRAME:")
print(df)
```

Then:

```python
print("LINE:")
print(line_text)
```

Then:

```python
print("SEARCH TARGET:")
print(search_target)
```

Then:

```python
print("FIELD:")
print(field)

print("VALUE:")
print(value)
```

These aren't permanent production features.

They're **diagnostic checkpoints**.

---

# 13. Images need visual debugging

You can't meaningfully inspect an image with:

```python
print(thresh)
```

Instead:

```python
cv2.imwrite(
    "debug_threshold.png",
    thresh
)
```

Then open the file.

Your debugging workflow becomes:

```text
Code
 ↓
Generate intermediate image
 ↓
Open image
 ↓
Look at it
 ↓
Compare with original
```

This is universal.

For video processing, save frames.

For PDFs, inspect rendered pages.

For audio, inspect waveforms/transcripts.

For APIs, print/log JSON.

For databases, inspect query results.

---

# 14. Debugging is controlled experimentation

Bad:

```text
Change PSM
Change threshold
Change resize
Change regex
Change Pandas
Change matching
Run
```

Now you don't know what fixed or broke it.

Good:

```text
Test original
 ↓
Test grayscale
 ↓
Test upscaled
 ↓
Test threshold
```

One variable at a time.

That gives you evidence.

---

# 15. Tesseract vs Pandas

This distinction is important.

Tesseract:

```python
ocr_data = pytesseract.image_to_data(...)
```

actually performs OCR.

Pandas:

```python
df = pd.DataFrame(ocr_data)
```

organizes the OCR result.

If Tesseract gives:

```text
566
```

Pandas will normally show:

```text
566
```

So if:

```text
Tesseract → 566
Pandas   → 566
```

don't start rewriting Pandas.

The problem is earlier.

---

# 16. Line reconstruction is a separate stage

Suppose Tesseract returns:

```text
Invoice:-
12345
```

Your application might reconstruct:

```text
Invoice:- 12345
```

That's useful.

But if your application creates:

```text
Invoice:--12345
```

then you have a **text reconstruction/normalization problem**.

That's different from OCR recognition.

So again:

```text
Tesseract
   ↓
"Invoice:-"
"12345"

Line grouping
   ↓
"Invoice:- 12345"

Normalization
   ↓
"Invoice:- 12345"
```

Print after every step.

---

# 17. Keyword matching is another independent stage

Suppose:

```text
line_text = "Invoice:- 12345"
search_target = "invoice"
```

Normalize:

```text
line_text:
invoice:- 12345

search_target:
invoice
```

Then:

```python
if search_target in searchable_line:
```

should match.

Debug it:

```python
print("SEARCH:", search_target)
print("LINE:", searchable_line)

print(
    "MATCH:",
    search_target in searchable_line
)
```

Now you know whether the matching logic is actually broken.

---

# 18. `Amount` vs `Total Amount` is a requirement question

This is not necessarily an OCR problem.

Suppose the image says:

```text
Total Amount:- 590
```

and the user searches:

```text
Amount
```

Should it match?

There are two possible rules.

### Rule A — substring

```text
Amount
    ↓
Total Amount
    ↓
MATCH
```

### Rule B — exact field

```text
Amount
    ↓
Total Amount
    ↓
NO MATCH
```

Neither is automatically correct.

The requirement must define it.

This is an important development lesson:

> **Some bugs are actually unclear requirements.**

---

# 19. POST and GET responsibilities

Think of them as two different jobs.

### POST

```text
POST /extract-custom-words/
```

means:

> Process this image.

```text
Image
 ↓
OCR
 ↓
Extract
 ↓
Create result
 ↓
Store latest result
```

### GET

```text
GET /ocr-result/
```

means:

> Show me the latest result.

```text
GET
 ↓
Read latest result
 ↓
Return it
```

So your current:

```python
return latest_ocr_response
```

is conceptually correct.

If you want:

```json
{
  "field": "Invoice",
  "value": "12345"
}
```

instead of:

```json
{
  "found_word": "Invoice:- 12345"
}
```

the better place to change that is the **OCR processing/service logic**.

GET should not re-interpret the OCR result.

---

# 20. Stateless does not mean "everything in one file"

Stateless means you aren't depending on persistent server-side session state/database state for the request workflow.

You can still have:

```text
routes/
controllers/
services/
utils/
config/
```

A stateless application can still have excellent architecture.

---

# 21. Your `latest_ocr_response`

Currently you have something like:

```python
latest_ocr_response = response
```

Then:

```text
POST
 ↓
latest_ocr_response
 ↓
GET
```

This works for your prototype.

But remember:

```text
Restart FastAPI
 ↓
Memory cleared
 ↓
latest_ocr_response disappears
```

That's not necessarily a problem right now.

If later your requirement becomes:

> "Users should retrieve OCR results from yesterday."

then you need persistent storage.

That's when a database becomes relevant.

---

# 22. Manual coding workflow

For any new task:

## Phase 1 — Understand

Write:

```text
Input:
Processing:
Output:
Errors:
```

## Phase 2 — Design

Draw:

```text
Input
 ↓
Step 1
 ↓
Step 2
 ↓
Step 3
 ↓
Output
```

## Phase 3 — Build minimum version

Don't build everything.

## Phase 4 — Test

Use known input.

## Phase 5 — Debug

Inspect intermediate states.

## Phase 6 — Add functionality

One feature at a time.

## Phase 7 — Refactor

Move working code into folders.

## Phase 8 — Regression test

Make sure refactoring didn't break behavior.

---

# 23. How to use AI without becoming dependent on it

This is especially important for you as a developer.

Don't use AI like:

> "Here's 500 lines. Fix everything."

Instead, investigate first.

For example:

```text
Expected:
GST = 90

Actual:
GST = 98
```

Then test:

```text
Original → 98
Grayscale → 98
Upscaled → 90
Threshold → 98
```

Now ask AI:

> "I tested four preprocessing versions. Only upscaled produces GST=90. What does this evidence suggest?"

That's a much stronger question.

You're still doing the engineering.

AI is helping you reason.

---

# 24. A good AI debugging prompt

Use this structure:

```text
I expected:

<expected result>


I actually received:

<actual result>


My pipeline is:

<step 1>
<step 2>
<step 3>


I tested:

Test 1 → result
Test 2 → result
Test 3 → result


The first stage where I believe
the result becomes wrong is:

<stage>


Don't rewrite the whole project.

Explain the likely cause,
how to verify it,
and give me the smallest change to test.
```

This will generally produce much more useful assistance than:

```text
"Fix my code."
```

---

# 25. Ask AI "why", not only "what"

When AI gives you code, ask:

```text
Why does this fix the problem?
```

Then:

```text
What evidence confirms this?
```

Then:

```text
How can I test it?
```

Then:

```text
What could this change break?
```

That forces you to understand the solution.

---

# 26. Universal debugging hierarchy

When something goes wrong, inspect in this order:

```text
1. Requirement
       ↓
2. Input
       ↓
3. First transformation
       ↓
4. Intermediate data
       ↓
5. Business logic
       ↓
6. Output formatting
       ↓
7. API/UI
```

Don't automatically debug from the bottom.

The final API response is often just **where you noticed the problem**.

It may not be where the problem started.

---

# 27. Common developer mistakes to avoid

### Mistake 1

Changing five things simultaneously.

**Fix:** One variable at a time.

### Mistake 2

Blaming the final layer.

**Fix:** Find the first incorrect state.

### Mistake 3

Assuming a library is wrong.

**Fix:** Print its input/output.

### Mistake 4

Overengineering too early.

**Fix:** Make the core logic work first.

### Mistake 5

Blindly copying AI code.

**Fix:** Understand and test every significant change.

### Mistake 6

Not defining expected output.

**Fix:** Write the expected result first.

### Mistake 7

Destroying a working version during experimentation.

**Fix:** Git commit before major experiments.

---

# 28. Git as part of debugging

Since you're working solo, Git is also a debugging tool.

Suppose:

```text
development
```

is working.

Create an experiment:

```text
experiment/ocr-threshold
```

Test thresholding.

If it fails:

```text
discard/revert
```

Try:

```text
experiment/ocr-upscale
```

If it works:

```text
commit
```

This gives you a safe baseline.

The principle is:

```text
Known working version
        ↓
Experiment
        ↓
Test
        ↓
Keep OR discard
```

---

# 29. A universal debugging checklist

When you see an error:

```text
[ ] What did I expect?
[ ] What did I actually get?
[ ] Can I reproduce it?
[ ] Where is the first incorrect result?
[ ] Can I print the intermediate value?
[ ] Can I save the intermediate file?
[ ] Can I test one variable at a time?
[ ] Is the input correct?
[ ] Is the transformation correct?
[ ] Is the business rule correct?
[ ] Is the output formatting correct?
[ ] Did my change actually fix the root cause?
[ ] Did it break another test?
```

---

# 30. Your strongest debugging habit

Learn to say:

> **"I don't know yet."**

That's not weakness.

It's the correct starting point.

Then gather evidence.

Instead of:

> "Maybe Pandas is wrong."

Do:

```python
print(df)
```

Instead of:

> "Maybe preprocessing is wrong."

Do:

```python
cv2.imwrite("debug_threshold.png", thresh)
```

Instead of:

> "Maybe keyword matching is broken."

Do:

```python
print(search_target)
print(searchable_line)
print(search_target in searchable_line)
```

Instead of:

> "Maybe Tesseract is wrong."

Test:

```text
Original
Grayscale
Upscaled
Threshold
```

Then compare.

---

# 31. The development loop to memorize

This is the one I recommend you actually memorize:

```text
UNDERSTAND
     ↓
DEFINE EXPECTED OUTPUT
     ↓
DESIGN THE PIPELINE
     ↓
BUILD SMALL
     ↓
RUN
     ↓
OBSERVE
     ↓
COMPARE EXPECTED vs ACTUAL
     ↓
FIND FIRST WRONG STAGE
     ↓
FORM A HYPOTHESIS
     ↓
CHANGE ONE THING
     ↓
TEST
     ↓
CONFIRM
     ↓
REFACTOR
     ↓
DOCUMENT
```

Then repeat.

---

# 32. Apply that loop to your OCR project

You started with:

```text
"Build OCR API"
```

Then encountered:

```text
OCR values wrong
```

Instead of randomly changing code:

```text
Expected:
500 / 90 / 590

Actual:
566 / 98 / 598
```

Then:

```text
Test preprocessing
```

Results:

```text
Original  → mostly correct
Grayscale → mostly correct
Upscaled  → correct
Threshold → wrong
```

Then:

```text
Remove threshold from current OCR pipeline
```

Then continue:

```text
Raw Tesseract
 ↓
DataFrame
 ↓
Line grouping
 ↓
Normalization
 ↓
Keyword matching
 ↓
Field/value extraction
```

That is proper debugging.

---

# 33. The mental model for every future project

Whether you're building:

```text
FastAPI
Flask
Node.js
PostgreSQL
OCR
Web scraper
AI agent
File automation
Payment integration
Background worker
```

the same thinking applies:

```text
INPUT
  ↓
TRANSFORM
  ↓
TRANSFORM
  ↓
BUSINESS LOGIC
  ↓
OUTPUT
```

When the output is wrong:

```text
Don't stare only at OUTPUT.

Inspect every transformation
until you find the FIRST wrong state.
```

That is the transferable skill.

---

# 34. Your project progression should be

For this OCR project specifically:

```text
Stage 1
Single-file working API
        ↓
Stage 2
Reliable preprocessing
        ↓
Stage 3
Reliable Tesseract configuration
        ↓
Stage 4
Reliable raw OCR data
        ↓
Stage 5
Reliable line reconstruction
        ↓
Stage 6
Reliable normalization
        ↓
Stage 7
Reliable keyword matching
        ↓
Stage 8
Reliable field/value extraction
        ↓
Stage 9
Correct JSON response
        ↓
Stage 10
GET latest result
        ↓
Stage 11
Testing
        ↓
Stage 12
Refactor into folders
        ↓
Stage 13
Documentation
        ↓
Stage 14
Deployment
```

**Don't jump to Stage 12 while Stage 5 is still broken.**

That's where a lot of developers waste time.

---

# 35. The biggest thing I want you to take from this

You don't need to become someone who memorizes every Python, FastAPI, OpenCV, Pandas, or Tesseract function.

You need to become someone who can look at:

```text
Expected ≠ Actual
```

and calmly say:

```text
Okay.

What went in?
What came out?
What happened in between?
Where did it first become wrong?
How can I prove that?
What's the smallest change I can test?
```

Once you develop that habit, debugging becomes much less intimidating.

**That's the real development skill you're building through this OCR project.**
