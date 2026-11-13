## Variables
- Python variables are used to store data values.
- You don’t need to declare a type. Python automatically assigns it based on the value.
Variables can hold different data types like numbers, strings, and lists.
- Must start with letters are underscore and can't start with numbers
- camel, pascal, snake case 
```python
my_variable="test" # ✅
20_variable = 20 # ❌
userFirstName = "Kali" #camel
UserMiddleName = "das" #pascal
User_Last_Name = "S" #snake
```

## Data Types
- Data type refers to the type of value a variable can store and how that value can be used in a program.
- It tells Python whether the data is a number, text, collection, true/false, etc.
- Data types help Python perform correct operations on the data.
- Common types: int, float, str, bool, list, tuple, dict, set.
```python
a = 10            # int
b = 10.5          # float
c = "Hello"       # str
d = True          # bool
e = [1, 2, 3]     # list
f = (1, 2, 3)     # tuple
g = {"a": 1}      # dict
h = {1, 2, 3}     # set

print(type(a), type(b), type(c), type(d))
print(type(e), type(f), type(g), type(h))
```

## Type Conversion (Casting)
- Type conversion means changing one datatype to another.
- int(), float(), str(), bool() are common casting functions.
- Important: invalid conversion causes ValueError (e.g., int("abc")).
```python
# String to int
print("100" + 20)  # 120

# String to float
print(float("99.99"))

# Int to string
print("Number is " + str(50))
```

## Operators 
- Operators are symbols that tell Python to perform a specific action on variables or values.
- They are used to perform tasks like addition, comparison, assignment, logical decisions, bit-level operations, etc.
1. Arithmetic Operators → (+, -, *, /, %, //, **)
2. Relational/Comparison Operators → (==, !=, >, <, >=, <=)
3. Logical Operators → (and, or, not)
4. Bitwise Operators → (&, |, ^, ~, <<, >>)
5. Assignment Operators → (=)
6. Compound/Augmented Operators → (+=, -=, *=, etc.)
7. Membership Operators → (in, not in)
8. Identity Operators → (is, is not)
```python
# 1) Arithmetic Operator
print("Arithmetic (+):", 10 + 5)

# 2) Relational / Comparison Operator
print("Relational (>):", 10 > 7)

# 3) Bitwise Operator
print("Bitwise (&):", 5 & 3)   # 5=0101, 3=0011

# 4) Logical Operator
print("Logical (and):", (22 > 18) and True)

# 5) Assignment Operator (must assign to show use)
x = 100
print("Assignment (=):", x)

# 6) Compound / Augmented Operator
y = 10
y += 5
print("Compound (+=):", y)

# 7) Membership Operator
print("Membership (in):", 20 in [10, 20, 30])

# 8) Identity Operator
print("Identity (is):", [1, 2, 3] is [1, 2, 3])  # False (different objects)
```

## Control Structures
- Conditional Statements (if, elif, else)
- Loops (for, while)
- break, continue, and pass
## Conditional Statements
- Conditional statements are used to make decisions in a program based on a condition (True/False).
```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#  if-else Ternary Expression (One-line if else)
value_if_true if condition else value_if_false
print("Even" if 10 % 2 == 0 else "Odd")
```

## while loop
- Repeats a block until condition becomes False
- break: stops the loop immediately
- continue: skips current iteration and goes to next
```python
i = 1
while i <= 5:
    print("i =", i)
    i += 1
```

## For Loop
```python
# range() is memory-efficient because it doesn’t create the full list upfront
range(start, stop, step)

print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(2, 6)))      # [2, 3, 4, 5]
print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]

# for Loop
langs = ["Python", "Java", "Go"]
for i, val in enumerate(langs):
    print(i, val)

d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)

# break, continue, pass
# continue - Skips the rest of the code in the current iteration. Jumps directly to the next iteration of the loop
# pass - Does nothing. It’s a placeholder statement (keeps syntax valid). Execution continues normally in the same iteration
nums = [2, 4, 7, 8]
for x in nums:
    if x % 2 == 1:
        print("First odd:", x)
        break
    elif x == 3:
        continue
    print(x)
```

## Strings
- String in Python is an immutable sequence of Unicode characters.
- Immutable = once created, you can’t change it in-place (you create a new string instead).
```python
s = "Python"  # """triple quotes multi-line string""" 'single quotes'
print(len(s))     # 6
print(s[0])       # 'P'
print(s[-1])      # 'n' (last char)

name = "Kalidas"
age = 26
print(f"{name} is {age} years old")  # Kalidas is 26 years old

# Concatenation and repetition
print("Py" + "thon")      # Python
print("Py" * 3)      # PyPyPy

# Membership (true/false)
print("th" in "Python")   # True

s = "Interview"
print(s[0:4])     # Inte
print(s[:4])      # Inte
print(s[4:])      # rview
print(s[::-1])    # weivretnI (reverse)
print(s[::2])     # Iteiw (every 2nd char)

# Case and whitespace
s = "  Hello World  "
print(s.strip())        # "Hello World"
print(s.lower())        # "  hello world  "
print(s.upper())        # "  HELLO WORLD  "
print(s.title())        # "  Hello World  "

# Search / check
s = "python programming"
print(s.find("pro"))     # 7 (index) / -1 if not found
print(s.startswith("py"))# True
print(s.endswith("ing")) # True

# Replace / split / join
s = "a,b,c"
parts = s.split(",")         # ['a', 'b', 'c']
print(" | ".join(parts))     # a | b | c

msg = "I like Java"
print(msg.replace("Java", "Python"))  # I like Python

# Validation
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True

result = "".join(["a", "b", "c"]) # abc
```

## Exceptions
- Python exceptions are runtime errors that can be caught and handled gracefully using try, except, else, and finally blocks. They prevent programs from crashing and allow developers to respond to unexpected situations like invalid input, missing files, or division by zero

```python
def process_data():
    # IndexError
    try:
        nums = [1, 2, 3]
        print(nums[5])   # invalid index
    except IndexError:
        print("Caught IndexError: Invalid list index.")

    # ValueError
    try:
        val = int("abc") # invalid conversion
    except ValueError:
        print("Caught ValueError: Invalid value for conversion.")

    # TypeError
    try:
        result = "abc" + 5  # wrong type
    except TypeError:
        print("Caught TypeError: Wrong type used in operation.")

    # KeyError
    try:
        data = {"name": "Kalidas"}
        print(data["age"])  # missing key
    except KeyError:
        print("Caught KeyError: Dictionary key not found.")

    # ZeroDivisionError
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: Division by zero.")

    # FileNotFoundError
    try:
        with open("missing.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Caught FileNotFoundError: File not found.")

process_data()
```

## File Handling
- Opening Files → open("file", "mode")
- Reading Files → read(), readline(), iteration
- Writing/Appending → "w" and "a" modes
- Editing Files → read → modify → write back
- Different Extensions → JSON handling with json.dump()
- With Statement → ensures file auto-closes safel

```python
# --- Opening and Writing to a File ---
f = open("example.txt", "w")   # "w" mode creates/overwrites
f.write("Hello, this is line 1\n")
f.write("This is line 2\n")
f.close()

# --- Reading the File ---
f = open("example.txt", "r")
print("File content using read():")
print(f.read())   # Reads entire file
f.close()

# --- Appending to the File ---
f = open("example.txt", "a")   # "a" mode appends
f.write("This is an appended line\n")
f.close()

# --- Reading Line by Line ---
f = open("example.txt", "r")
print("File content using readline():")
print(f.readline())   # Reads first line
print(f.readline())   # Reads second line
f.close()

# --- Editing File (Read + Rewrite) ---
f = open("example.txt", "r")
data = f.read()
f.close()

# Replace text and write back
f = open("example.txt", "w")
f.write(data.replace("line", "sentence"))
f.close()

# --- Working with Different Extensions ---
import json

data = {"name": "Kalidas", "role": "Developer"}
with open("data.json", "w") as f:   # JSON file
    json.dump(data, f)

# --- Using 'with' Statement (auto-closes file) ---
with open("example.txt", "r") as f:
    print("File content with 'with':")
    for line in f:
        print(line.strip())
```        