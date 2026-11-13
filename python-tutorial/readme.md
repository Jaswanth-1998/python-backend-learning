## Introduction
Python is a high‑level, interpreted, and general‑purpose programming language known for its readability and simplicity. 
It supports multiple programming paradigms, has a rich library ecosystem, and is widely used in web development, automation, data science, and artificial intelligence.

## Why Python is Popular?
- Easy to learn and read
  - Python’s syntax is clean and looks like English. This helps beginners learn programming quickly.
- Interpreted language
  - You don’t need to compile. The code runs line by line, making debugging easier.
- Dynamically typed
  - You don’t need to declare data types explicitly.
- Large Standard Library
  - Comes with built‑in modules for file handling, math, networking, etc.
- Huge Community Support
  - Millions of developers, tutorials, and libraries available.

## Where is Python Used?
- Web Development
  - Django, Flask
- Data Science & Machine Learning
  - Pandas, NumPy
- Artificial Intelligence
    - Deep learning models, Natural language processing
- Automation / Scripting
  - Automate tasks, Write simple bots, System scripts
- Game Development
   - Pygame
- Software Development
   - Backend systems, APIs


## Print Function (print())
- print() is used to display output on the console.
- Python supports easy formatting using f-strings (recommended in interviews).
```python
name = "Kalidas"
print(f"My name is {name}")   # f-string
```

## Input from User (input())
- input() always returns data as a string.
- If you need numbers, you must convert it using int() / float().
```python
name = input("Enter your name: ")
print("Welcome,", name)
```

##  First Program
- Demonstrates basics: print(), input(), variables, type conversion, and arithmetic.
- This is a common beginner interview test to verify fundamentals.
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)
```
## Collections or Basic Data Structures
- Lists
- Tuples
- Sets
- Dictionaries

## List
- A list is an ordered, changeable (mutable) collection that allows duplicate values.
- Lists can store different data types (int, string, objects) in a single structure.
- Lists are widely used for storing, iterating, updating, and managing collections of data.

## Tuple
- A tuple is an ordered, unchangeable (immutable) collection that allows duplicates.
- Once created, tuple values cannot be modified (no add/remove/update).
- Tuples are faster than lists and used for fixed data.

## Set
- A set is an unordered, mutable collection that stores unique values (no duplicates).
- Sets are useful for removing duplicates and performing mathematical operations.
- Sets do not support indexing because they are unordered.

## Dictionary
- A dictionary is an unordered, mutable collection that stores data in key-value pairs.
- Keys are unique and used to access, update, or delete values efficiently.
- Dictionaries are widely used to represent structured data like user details, API responses, and configurations.

## OOP Concepts in Python
### Classes & Objects
- **Class:** A blueprint that defines attributes (variables) and behaviors (methods).
- **Object:** An instance of a class, representing a specific entity created from that blueprint.
### Method Calls
- A method is a function defined inside a class.
- **Method call:** Invoking that function using an object (e.g., obj.method()).
### Inheritance (Single, Multiple, Multilevel)
- **Definition:** Mechanism where a child class acquires properties and methods of a parent class.
- Types:
  - Single: One child inherits from one parent.
  - Multiple: Child inherits from multiple parents.
  - Multilevel: A chain of inheritance (grandparent → parent → child).
### Overloading (Method Overloading via default args)
- **Definition:** Defining methods with the same name but different parameter handling.
- In Python, achieved using default arguments or *args/**kwargs since true compile-time overloading isn’t supported.
### Overriding
- **Definition:** Redefining a parent class method in the child class with the same name and signature.
- Happens at runtime and supports polymorphism.
### Data Hiding (Encapsulation)
- **Definition:** Restricting direct access to class variables/methods to protect data integrity.
- In Python, achieved using private members (prefix __) and getter/setter methods
### Operator Overloading
- **Definition:** Redefining how operators (+, -, *, etc.) work for user-defined objects.
- Achieved by implementing special methods like __add__, __sub__, etc.

- **Overloading vs Overriding:** Overloading = same name, different parameters (compile-time). Overriding = child redefines parent method (runtime).
- **Encapsulation:** Protects data by controlling access.
- **Polymorphism:** Same interface, different implementations (via overriding or operator overloading).