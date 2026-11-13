# Python Backend Developer Interview Preparation -- Resume-Based Question Bank

**Candidate:** Jaswanth S.\
**Target role:** Python Backend Developer\
**Target experience level:** 2--4 years\
**Basis:** Questions tailored to the uploaded resume.

------------------------------------------------------------------------

## 1. Initial assessment of the resume

### Technical profile

-   **Programming:** Python, SQL
-   **Backend:** Flask, FastAPI, RESTful API development, CRUD
    operations
-   **Database:** PostgreSQL, SQLAlchemy ORM, database design and
    integration
-   **Libraries:** Pandas, Flask-Migrate
-   **Web:** HTML, Bootstrap, Jinja2, AJAX
-   **Reporting:** PDF generation, Excel report generation, data
    processing, HTML dashboards
-   **Testing:** Manual, functional, system, end-to-end testing,
    retesting, defect tracking
-   **Practices:** OOP, debugging, exception handling, requirement
    analysis, SDLC, STLC
-   **Projects:** NIC Assessment Management System, IPMS, TNRD, LoanPal,
    ModeAlpha

### Initial interview concern

The resume describes 3+ years of overall experience, but previous roles
emphasize manual testing, while the current NIC project describes
backend development.

An interviewer is likely to investigate how much production Python
development you personally performed, what code you owned, and whether
you can independently implement features.

This is not necessarily a weakness. You must, however, be able to
demonstrate your actual development experience and distinguish your own
contributions from the team's work.

------------------------------------------------------------------------

## 2. Round 1 -- Python fundamentals

These questions establish whether you understand Python beyond syntax.

### Basic to intermediate questions

1.  What are the differences between a list, tuple, set, and dictionary?
2.  What is mutable and immutable in Python?
3.  What is the difference between `is` and `==`?
4.  Explain shallow copy and deep copy.
5.  What are `*args` and `**kwargs`?
6.  What is the difference between `return`, `yield`, and `pass`?
7.  What are Python decorators? Where have you used them?
8.  What are lambda functions?
9.  Explain list comprehension and dictionary comprehension.
10. What is the difference between an iterator and a generator?
11. What is exception handling? Explain `try`, `except`, `else`, and
    `finally`.
12. What is the difference between a module and a package?
13. Explain OOP concepts in Python.
14. What is inheritance? What is method overriding?
15. What is the difference between instance methods, class methods, and
    static methods?

### Practical coding questions

16. Write a Python program to find duplicate elements in a list.
17. Find the second-largest number in a list.
18. Reverse a string without using slicing.
19. Count the frequency of each character in a string.
20. Remove duplicate dictionaries from a list based on an ID.
21. Find common elements between two lists.
22. Sort a list of dictionaries by a particular key.
23. Read a JSON file and extract specific fields.
24. Write a function that validates an email address.
25. Write a function that groups transactions by customer ID.

**What the interviewer evaluates:** Can you write code independently,
explain its execution, handle edge cases, and understand time and space
complexity?

------------------------------------------------------------------------

## 3. Round 2 -- Flask and FastAPI

This is one of the most important rounds because both frameworks appear
in the resume.

### Framework fundamentals

1.  What is Flask? What is FastAPI?
2.  What are the major differences between Flask and FastAPI?
3.  When would you choose Flask over FastAPI?
4.  What is a Blueprint in Flask?
5.  What is dependency injection in FastAPI?
6.  What is Pydantic?
7.  What is request validation?
8.  What is middleware?
9.  What is the difference between middleware and decorators?
10. What is the purpose of `app.py` or `main.py`?
11. How do you manage environment variables?
12. How do you connect PostgreSQL with Flask and FastAPI?

### Real-world implementation questions

13. Explain how you would implement a user registration API using
    FastAPI.
14. How do you validate incoming JSON data?
15. How do you handle exceptions globally?
16. How do you implement authentication?
17. How do you implement role-based access control?
18. How do you handle file uploads?
19. How do you implement pagination?
20. How do you structure a large Flask application?
21. How do you separate routes, business logic, database operations, and
    validation?
22. How do you manage database connections in FastAPI?
23. What happens when an API receives 1,000 simultaneous requests?
24. What is the difference between synchronous and asynchronous
    programming?

### Essential practical question

Suppose the requirement is:

> Develop an API to register users, authenticate users, and retrieve
> user details.

Explain how you would develop this application from scratch. Cover:

-   Project structure
-   Database design
-   API endpoints
-   Request and response schemas
-   Service layer
-   Authentication
-   Validation
-   Exception handling
-   Testing

The interviewer may then ask you to implement one endpoint without AI
assistance.

------------------------------------------------------------------------

## 4. Round 3 -- REST API development

The resume explicitly mentions RESTful API development, so practical
knowledge is expected.

1.  What is REST architecture?
2.  What are HTTP methods?
3.  Difference between GET and POST.
4.  Difference between PUT and PATCH.
5.  What is idempotency?
6.  Explain HTTP status codes 200, 201, 204, 400, 401, 403, 404, 409,
    and 500.
7.  What is the difference between authentication and authorization?
8.  What is JWT?
9.  What are access tokens and refresh tokens?
10. How do you secure an API?
11. What is CORS?
12. What is API versioning?
13. How do you implement pagination and filtering?
14. How do you handle duplicate API requests?
15. How do you design consistent API response structures?

### Practical scenario

Suppose the application has a customer table. Design these APIs:

  Method   Endpoint                Purpose
  -------- ----------------------- -----------------
  POST     `/api/customers`        Create customer
  GET      `/api/customers`        List customers
  GET      `/api/customers/{id}`   Get customer
  PUT      `/api/customers/{id}`   Update customer
  DELETE   `/api/customers/{id}`   Delete customer

The interviewer may ask you to implement the POST and GET endpoints.

------------------------------------------------------------------------

## 5. Round 4 -- PostgreSQL and SQLAlchemy

This is a high-priority area because PostgreSQL and SQLAlchemy appear in
both work and personal project descriptions.

### PostgreSQL questions

1.  What is a primary key?
2.  What is a foreign key?
3.  What is a unique constraint?
4.  What is an index?
5.  What are database normalization rules?
6.  Explain 1NF, 2NF, and 3NF.
7.  Difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.
8.  What is GROUP BY?
9.  What is HAVING?
10. What is the difference between WHERE and HAVING?
11. What is a subquery?
12. What is a CTE?
13. What are database transactions?
14. Explain ACID properties.
15. What is database indexing, and when can an index hurt performance?

### SQL practical questions

Consider these tables.

**customers**

  id   name   phone
  ---- ------ ------------
  1    Arun   9876543210
  2    Ravi   9876543211

**payments**

  id   customer_id   amount
  ---- ------------- --------
  1    1             500
  2    1             700
  3    2             300

Write queries to:

1.  Retrieve all customers with their payments.
2.  Calculate the total payment for each customer.
3.  Find customers who haven't made any payments.
4.  Find the highest payment.
5.  Find customers whose total payments exceed 500.
6.  Retrieve the latest payment for each customer.

### SQLAlchemy questions

1.  What is SQLAlchemy ORM?
2.  Difference between ORM and raw SQL.
3.  What is a model?
4.  What is a relationship?
5.  Explain one-to-one, one-to-many, and many-to-many relationships.
6.  What is `db.session.add()`?
7.  What is `db.session.commit()`?
8.  Difference between `flush()` and `commit()`.
9.  What is `rollback()`?
10. What is lazy loading?
11. What is the N+1 query problem?
12. What is Flask-Migrate?
13. How do you handle database IntegrityError?
14. How do you manage transactions when multiple tables need updating?

------------------------------------------------------------------------

## 6. Round 5 -- Questions directly from the projects

This is where an interviewer is likely to spend considerable time. The
personal projects provide concrete areas to investigate.

### Project 1: NIC Assessment Management System

The resume describes a FastAPI assessment application with PostgreSQL,
HTML dashboards, and PDF/Excel reporting.

Questions:

1.  Explain the complete architecture of your assessment management
    system.
2.  What modules did you develop?
3.  What was your individual contribution?
4.  How did you design the database?
5.  How did you connect FastAPI with PostgreSQL?
6.  How did you retrieve assessment data?
7.  How did you generate PDF reports?
8.  Which Python libraries did you use for PDF generation?
9.  How did you generate Excel reports?
10. How did you handle large assessment datasets?
11. How did you calculate assessment results?
12. How did you handle concurrent users?
13. How did you validate assessment submissions?
14. How did you handle database failures?
15. How did you test the APIs?
16. How did you deploy the application?
17. What was the most difficult bug you encountered?
18. What improvements would you make to the application?

**Follow-up scenario:** Suppose 500 candidates submit their assessments
simultaneously. How would you ensure that submissions are saved
correctly and duplicate submissions are prevented?

A strong answer should discuss database transactions, unique constraints
or idempotency, concurrency, and error handling.

### Project 2: LoanPal -- Flask and PostgreSQL

This project involves real business logic.

Questions:

1.  Explain the complete workflow of LoanPal.
2.  How did you design Customer, Loan, Payment, and Expenditure models?
3.  How did you calculate loan interest?
4.  How did you calculate outstanding balances?
5.  How did you handle partial payments?
6.  How did you manage multiple loans for one customer?
7.  How did you implement customer authentication?
8.  How did you prevent unauthorized access to another user's records?
9.  How did you implement CRUD operations?
10. How did you handle duplicate customer phone numbers?
11. How did you implement soft deletion, if applicable?
12. How did you manage database relationships?
13. How did you calculate daily collections?
14. How did you generate financial reports?

**Follow-up scenario:** A customer has a loan amount of ₹50,000 and
makes three payments: ₹5,000, ₹10,000, and ₹8,000.

-   How would you calculate the total collected amount and outstanding
    principal?
-   What would you do if the second payment were accidentally recorded
    twice?

The interviewer assesses business logic, database design, and data
integrity.

### Project 3: ModeAlpha -- Mock Test Management System

This project is useful for demonstrating backend architecture.

Questions:

1.  Explain the complete architecture of ModeAlpha.
2.  Why did you choose Flask instead of FastAPI?
3.  Why did you use function-based routes?
4.  How did you implement separate admin and user workflows?
5.  How did you implement session authentication?
6.  How did you implement approval-based login?
7.  How did you import questions from Word documents?
8.  How did you store questions and answers?
9.  How did you implement question navigation?
10. How did you implement pause and resume?
11. How did you track answered, unanswered, and marked questions?
12. How did you implement test timers?
13. How did you calculate final scores?
14. How did you implement negative marking?
15. How did you implement pagination?
16. What is soft deletion, and why did you use it?
17. How did you implement AJAX interactions?
18. How did you handle multiple users taking the same examination?
19. How did you prevent users from accessing admin functionality?
20. How did you handle browser refresh during an examination?

**Follow-up scenario:** A user starts an examination and answers 10
questions. Suddenly, their browser crashes. When they log in again, how
will you restore their examination progress?

A strong answer should explain database persistence, examination attempt
records, saved answers, timestamps, and server-side validation.

------------------------------------------------------------------------

## 7. Round 6 -- Debugging and real-world scenarios

This round distinguishes someone who can read existing code from someone
who can independently maintain a backend application.

  -----------------------------------------------------------------------
  Scenario                            Interview question
  ----------------------------------- -----------------------------------
  Database failure                    Your application cannot connect to
                                      PostgreSQL. How do you investigate?

  Slow API                            An API takes 15 seconds to respond.
                                      How do you identify the bottleneck?

  Duplicate records                   Two requests create the same
                                      customer. How do you prevent this?

  Production error                    An API suddenly returns HTTP 500.
                                      Where do you start?

  Memory issue                        Your application consumes
                                      increasing memory. How do you
                                      investigate?

  Incorrect data                      Your report displays incorrect
                                      payment totals. How do you debug
                                      it?

  Authentication                      A user can access another user's
                                      records. How do you fix it?

  Concurrent requests                 Multiple users update the same
                                      record. How do you maintain
                                      consistency?
  -----------------------------------------------------------------------

Additional questions:

1.  How do you read a Python traceback?
2.  How do you use Python logging?
3.  What is the difference between debugging and exception handling?
4.  How do you reproduce a production bug locally?
5.  How do you identify whether an issue is in the API, database, or
    frontend?
6.  How do you write meaningful error messages?
7.  How do you avoid exposing sensitive information in logs?

------------------------------------------------------------------------

## 8. Round 7 -- Testing and software development practices

The resume includes functional testing, requirement analysis, defect
tracking, and retesting.

1.  What is the difference between unit testing and integration testing?
2.  What is pytest?
3.  How do you test a Flask API?
4.  How do you test a FastAPI endpoint?
5.  What is mocking?
6.  What is test coverage?
7.  How do you test invalid input?
8.  How do you test database operations?
9.  What is regression testing?
10. What is the difference between functional and non-functional
    testing?
11. Explain your defect lifecycle.
12. How do you collaborate with testers and developers?
13. What happens during code review?
14. What is Git branching?
15. Explain the development, testing, and production deployment
    workflow.

------------------------------------------------------------------------

## 9. Round 8 -- Advanced questions for a 3+ year candidate

These questions help determine whether you understand production backend
development.

  Topic                   Questions
  ----------------------- ------------------------------------------------
  Architecture            Monolithic vs microservices?
  Database                Connection pooling and transaction isolation?
  Performance             Redis caching and query optimization?
  Security                SQL injection, password hashing, CSRF and XSS?
  Concurrency             Multithreading vs multiprocessing vs asyncio?
  Deployment              Docker, Gunicorn, Uvicorn and Nginx?
  Scalability             Horizontal vs vertical scaling?
  Background processing   Celery and task queues?
  API                     Rate limiting and API versioning?
  Monitoring              Logging, health checks and monitoring?

You are not expected to be an expert in every advanced topic. You should
understand the fundamentals and explain where you have actually used
them. Be clear about the difference between hands-on experience and
conceptual knowledge.

------------------------------------------------------------------------

## 10. The 15 highest-priority interview questions

If the interviewer has only 45--60 minutes, these are likely high-value
questions:

1.  Explain your current NIC Assessment Management System architecture.
2.  What is the difference between Flask and FastAPI?
3.  Explain Python decorators with an example.
4.  Explain mutable and immutable objects.
5.  How do you structure a scalable Flask application?
6.  How do you implement JWT authentication in FastAPI?
7.  Explain SQLAlchemy session management.
8.  Write a SQL query to find customers with no payments.
9.  How do you handle database transactions and rollback?
10. How did you implement question navigation and pause/resume in
    ModeAlpha?
11. How would you prevent duplicate examination submissions?
12. An API returns HTTP 500. How do you debug it?
13. How do you optimize a slow database query?
14. Explain the difference between authentication and authorization.
15. Describe a difficult bug you personally solved.

------------------------------------------------------------------------

## 11. Interview evaluation priorities

Knowing the answers to 100 Python interview questions does not make
someone a strong backend developer.

For this experience level, the interviewer is likely to evaluate five
capabilities:

  Capability            Expected evidence
  --------------------- -------------------------------------------------
  Python coding         Write functions without depending on AI
  Backend development   Build APIs independently
  Database              Design tables and write queries
  Debugging             Investigate and fix unfamiliar errors
  Project ownership     Explain implementation decisions and trade-offs

The resume already provides three projects to discuss. The priority is
to understand every important part of those projects. Building many
additional projects is not a substitute for being able to explain and
defend the work already listed.

------------------------------------------------------------------------

# 12. Three interview styles -- complete practice format

Use all three styles. They test different capabilities and should not be
treated as interchangeable.

## Style A -- One question at a time, with follow-ups

**Purpose:** Test conceptual understanding, communication, depth of
knowledge, and the ability to defend technical decisions.

### How the interview works

1.  The interviewer asks exactly one question.
2.  You answer in your own words, without looking up a solution.
3.  The interviewer evaluates correctness, completeness, clarity, and
    practical relevance.
4.  The interviewer asks follow-up questions based on your answer.
5.  If your answer is incomplete, the interviewer probes the missing
    concept rather than immediately giving the solution.
6.  After the question and follow-ups, the interviewer gives feedback
    and a score.
7.  The interviewer moves to the next question.

### Example interview sequence

**Main question:** What is the difference between Flask and FastAPI?

Possible follow-ups:

-   What is ASGI, and how does it differ from WSGI?
-   Does FastAPI automatically make every endpoint asynchronous?
-   What happens if you call blocking code inside an async endpoint?
-   When would you choose Flask for a new project?
-   How would you migrate a Flask application to FastAPI?

### Evaluation criteria

-   Technical correctness
-   Depth of understanding
-   Practical examples
-   Ability to explain trade-offs
-   Ability to handle follow-up questions

**Important rule:** Do not memorize a prepared paragraph. Explain the
concept as if you are discussing a real implementation with another
developer.

------------------------------------------------------------------------

## Style B -- Coding and debugging focused

**Purpose:** Determine whether you can independently write, execute,
inspect, and repair Python backend code.

### Part 1: Python coding exercises

The interviewer gives a problem and expects you to:

1.  Clarify the requirement.
2.  Identify input and expected output.
3.  Think through the approach.
4.  Write a function.
5.  Test normal cases.
6.  Test edge cases.
7.  Explain time and space complexity where relevant.

Example problems:

-   Find duplicate values in a list.
-   Find the second-largest number.
-   Count character frequency.
-   Group payment records by customer ID.
-   Sort dictionaries by a selected field.
-   Validate a JSON payload.
-   Calculate the outstanding balance of a loan.
-   Remove duplicate records based on a unique identifier.

### Part 2: SQL coding

The interviewer may ask you to write queries for:

-   INNER JOIN and LEFT JOIN
-   GROUP BY and HAVING
-   Customers with no payments
-   Total payments by customer
-   Latest transaction per customer
-   Duplicate records
-   Pagination and filtering

### Part 3: Backend implementation

Implement one or more of the following:

-   Flask customer registration endpoint.
-   FastAPI GET endpoint with query parameters.
-   SQLAlchemy model and relationship.
-   API request validation.
-   Database transaction with rollback.
-   Consistent error response.

### Part 4: Debugging exercises

The interviewer gives you a faulty code snippet, error message, or
unexpected result.

For every debugging task, follow this process:

1.  Read the complete error and traceback.
2.  Identify the failing file, line, and operation.
3.  Understand the expected behavior.
4.  Reproduce the issue.
5.  Check inputs and intermediate values.
6.  Isolate whether the problem is in Python logic, API handling,
    database interaction, or configuration.
7.  Identify the root cause.
8.  Apply the smallest appropriate fix.
9.  Retest the original failure.
10. Check for regressions.

### Example debugging scenarios

  -----------------------------------------------------------------------
  Problem                             What you should investigate
  ----------------------------------- -----------------------------------
  `TypeError`                         Data types, function arguments,
                                      unexpected `None`

  `KeyError`                          Missing dictionary keys and input
                                      structure

  `IntegrityError`                    Unique constraints, foreign keys,
                                      duplicate inserts

  `OperationalError`                  Database connection and
                                      configuration

  HTTP 500                            Application traceback and failing
                                      operation

  Incorrect totals                    SQL aggregation, duplicate joins,
                                      business logic

  Slow endpoint                       Query count, indexes, external
                                      calls, processing time

  Duplicate submission                Request retries, transaction
                                      handling, constraints
  -----------------------------------------------------------------------

### Evaluation criteria

-   Problem-solving approach
-   Code correctness
-   Readability and maintainability
-   Edge-case handling
-   Debugging methodology
-   Understanding of root cause
-   Ability to test the fix

**Important rule:** Do not jump directly to a solution. Explain how you
identify the problem. In real backend development, systematic diagnosis
is as important as writing the final code.

------------------------------------------------------------------------

## Style C -- Project-based technical deep dive

**Purpose:** Verify that you actually understand the applications listed
in your resume and can explain your individual contributions.

The interviewer selects one project and investigates it from requirement
to implementation.

### Phase 1: Requirement understanding

Questions:

1.  What problem does the application solve?
2.  Who are its users?
3.  What are the main business workflows?
4.  What were the functional requirements?
5.  What were the technical constraints?
6.  Which parts did you personally develop?

### Phase 2: Architecture

Questions:

1.  Explain the complete folder structure.
2.  Why did you choose Flask or FastAPI?
3.  Why did you separate routes, services, models, and schemas?
4.  How does a request move through your application?
5.  Where is validation performed?
6.  Where is business logic implemented?
7.  How are database operations managed?
8.  How are errors handled?

### Phase 3: Database design

Questions:

1.  Explain your database tables.
2.  What are the primary and foreign keys?
3.  How are the tables related?
4.  Which columns have unique constraints?
5.  How do you prevent invalid records?
6.  How do you handle migrations?
7.  How do you optimize frequently executed queries?

### Phase 4: Feature implementation

The interviewer selects a feature and asks you to explain it step by
step.

Examples:

-   NIC: assessment submission and report generation.
-   LoanPal: loan creation, payment collection, and outstanding balance.
-   ModeAlpha: examination attempt, question navigation, and answer
    persistence.

You should explain:

1.  What triggers the feature?
2.  Which API or route handles it?
3.  What input does it receive?
4.  What validation happens?
5.  What business logic executes?
6.  Which database tables are accessed?
7.  What response is returned?
8.  What happens when something fails?

### Phase 5: Failure scenarios

The interviewer introduces unexpected situations:

-   Database connection fails.
-   Two users update the same record.
-   Duplicate submissions arrive.
-   A user refreshes the browser.
-   A report contains incorrect totals.
-   An API becomes slow.
-   An unauthorized user accesses a protected endpoint.

Explain the root cause you would investigate and the corrective
approach.

### Phase 6: Ownership and improvement

Questions:

1.  Which feature did you personally find most challenging?
2.  What was the most difficult bug you solved?
3.  What technical decision would you change today?
4.  What limitations did the original architecture have?
5.  What would you improve if the user base increased significantly?
6.  What did you learn from the project?

### Evaluation criteria

-   Genuine project ownership
-   Architecture understanding
-   Database knowledge
-   Business logic understanding
-   Ability to trace request execution
-   Debugging and failure handling
-   Technical decision-making
-   Honest communication about individual contribution

**Important rule:** Never claim that you implemented something if you
only tested, reviewed, or coordinated it. Explain exactly what you did
and what other team members handled.

------------------------------------------------------------------------

## 13. Recommended mock interview structure

Use the following structure for a full interview simulation.

  Stage   Focus                                        Suggested duration
  ------- ------------------------------------------ --------------------
  1       Introduction and resume discussion                    5 minutes
  2       Python fundamentals                                  10 minutes
  3       Flask and FastAPI                                    10 minutes
  4       REST APIs and PostgreSQL                             10 minutes
  5       Coding and debugging                                 15 minutes
  6       Project-based deep dive                              15 minutes
  7       Final technical and behavioral questions              5 minutes

This is a practice structure, not a guarantee of how every company
conducts interviews.

### Suggested scoring rubric

Score each area from 0 to 5:

  ----------------------------------------
            Score Meaning
  ---------------------------------------- 
         0 Unable to answer

         1 Very limited understanding

         2 Basic understanding,
         significant gaps

         3 Correct intermediate
          understanding

         4 Strong understanding with
           practical examples

         5 Thorough explanation,
           implementation knowledge, and
           sound trade-offs
  -------------------------------------------

Evaluate these areas separately:

-   Python fundamentals
-   Coding ability
-   Flask/FastAPI
-   REST API design
-   PostgreSQL and SQLAlchemy
-   Debugging
-   Project ownership
-   Testing and software practices
-   Communication and technical reasoning

Do not use the overall score alone. A high conceptual score cannot
compensate for an inability to write or debug code when the role
requires hands-on backend development.

------------------------------------------------------------------------

## 14. How to use this interview guide

Recommended preparation sequence:

1.  Study Python fundamentals and solve coding questions.
2.  Practise SQL and SQLAlchemy.
3.  Build or rebuild small Flask and FastAPI endpoints without copying
    solutions.
4.  Practise REST API design and authentication.
5.  Trace the complete request lifecycle in your own projects.
6.  Practise debugging from actual errors and tracebacks.
7.  Prepare detailed, truthful explanations of your individual project
    contributions.
8.  Complete all three mock interview styles.
9.  Review weak areas and repeat the exercises.

### Final recommendation

Start with the **Intermediate -- 2--4 years** difficulty.

Use the three interview styles for different purposes:

-   **One question at a time with follow-ups:** Test your knowledge and
    communication.
-   **Coding and debugging focused:** Test your ability to implement and
    troubleshoot.
-   **Project-based technical deep dive:** Test whether you genuinely
    own and understand your resume projects.

The objective is not to memorize answers. It is to demonstrate that you
can understand requirements, design a solution, write code, debug
failures, and explain your technical decisions independently.

------------------------------------------------------------------------

## Suggested filename

`Jaswanth_Python_Backend_Developer_Interview_Preparation.md`
