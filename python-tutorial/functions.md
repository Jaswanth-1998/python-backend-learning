## Functions
- **Definition & Call:** Functions are reusable blocks of code defined with def and executed by calling their name with parentheses.
- **Arguments & Defaults:** Functions accept inputs (positional/keyword) and can have default values.
- **Docstrings:** Triple-quoted strings inside a function describe its purpose.
- **Scope:** Variables inside functions are local; outside are global.
- **Recursion:** A function calling itself to solve problems step by step.
- **Functional Programming:** Functions are first-class objects — they can be passed, returned, or stored.

```python
x = 10  # global ( Outside function)
def myFunction(name, isAdmin=False): # Default Arguments (isAdmin=False)
    """Sample test function"""  # Docstrings
    x = 5  # local (Inside function)
    print("My Function")
    print(name, isAdmin)
    print(x)
    
myFunction("kalidas", True)
print(x)
```

## Lambda Function
- A lambda function is a small, anonymous function defined using the  keyword.
- It can take any number of arguments but has only one expression, which is evaluated and returned.
- Useful for short, throwaway functions where defining a full function would be overkill.

```python
square = lambda x: x * x
print(square(5))   # Output: 25

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)   # Output: [1, 4, 9, 16]

nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # Output: [10, 20, 30]
```

## Recursion
- Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem.
- It’s often used for problems that can be broken down into smaller, similar subproblems (like factorials, Fibonacci, or tree traversal).
- Key point: Every recursive function must have a base case to stop infinite calls.

```python
def factorial(n):
    if n == 0:   # base case
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

def fibonacci(n):
    if n <= 1:   # base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8
```

## Higher-Order Functions
-  Functions that take other functions as arguments or return them.

### Function as a Parameter
- Passing a function into another function.
```python
def greet(name):
    return f"Hello, {name}"

def call_func(func, value):
    return func(value)

print(call_func(greet, "Kalidas"))  # Hello, Kalidas
```
### Function as a Return Value
- A function can return another function
```python
def outer():
    def inner():
        return "Inner function called"
    return inner

fn = outer()
print(fn())   # Inner function called
```
### Closures
- A closure is a function that remembers variables from its enclosing scope even if that scope is gone.
```python
def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
print(double(5))   # 10
```
### Decorators
- A decorator is a function that modifies another function’s behavior without changing its code.
```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```
## built-in functions
```python
# Sample student data
students = [
    {"name": "Alice", "marks": [85, 90, 78]},
    {"name": "Bob", "marks": [60, 70, 65]},
    {"name": "Charlie", "marks": [95, 88, 92]}
]

# A: abs(), all(), any(), ascii()
print(abs(-10))                           # 10
print(all([True, 1, "non-empty"]))        # True
print(any([0, False, ""]))                # False
print(ascii("Café"))                      # 'Cafe'

# B: bin(), bool(), bytes()
print(bin(10))                            # '0b1010'
print(bool(0))                            # False
print(bytes("hello", "utf-8"))            # b'hello'

# C: callable(), chr(), complex()
print(callable(len))                      # True
print(chr(65))                            # 'A'
print(complex(2, 3))                      # (2+3j)

# D: dict(), dir(), divmod()
student_dict = dict(name="David", marks=[80, 85])
# print(dir(student_dict))                  # Shows attributes/methods
print(divmod(17, 5))                      # (3, 2)

# E: enumerate(), eval()
for i, s in enumerate(students, start=1):
    print(i, s["name"])
print(eval("5 + 10"))                     # 15

# F: filter(), float(), format()
passed = list(filter(lambda s: sum(s["marks"])/len(s["marks"]) >= 70, students))
print(passed)
print(float("3.14"))                      # 3.14
print(format(1234, ","))                  # '1,234'

# G: getattr(), globals()
# print(getattr(students[0], "get", None))  # <built-in method get>
# print(globals().keys())                   # Shows global symbols

# H: hasattr(), hash(), help(), hex()
print(hasattr(students[0], "keys"))       # True
print(hash("Python"))                     # Hash value
# help(str)                               # Shows documentation
print(hex(255))                           # '0xff'

# I: id(), input(), int(), isinstance()
print(id(students))                       # Memory address
# name = input("Enter your name: ")       # User input
print(int("42"))                          # 42
print(isinstance(3.14, float))            # True

# L: len(), list(), locals()
print(len(students))                      # 3
print(list("abc"))                        # ['a', 'b', 'c']
# print(locals().keys())                    # Local variables

# M: map(), max(), min()
averages = list(map(lambda s: sum(s["marks"])/len(s["marks"]), students))
print(max(averages))                      # Highest average
print(min(averages))                      # Lowest average

# N: next()
it = iter([1, 2, 3])
print(next(it))                           # 1

# O: oct(), open(), ord()
print(oct(64))                            # '0o100'
# with open("test.txt", "w") as f: f.write("Hello")
print(ord("A"))                           # 65

# P: pow(), print(), property()
print(pow(2, 5))                          # 32
print("Hello World")                      # Hello World

# R: range(), repr(), reversed(), round()
print(list(range(5)))                     # [0,1,2,3,4]
print(repr("Python"))                     # "'Python'"
print(list(reversed([1,2,3])))            # [3,2,1]
print(round(3.14159, 2))                  # 3.14

# S: set(), setattr(), slice(), sorted(), str(), sum(), super()
print(set([1,2,2,3]))                     # {1,2,3}
class Demo: pass
d = Demo()
setattr(d, "x", 100)
print(d.x)                                # 100
print([1,2,3,4][slice(1,3)])              # [2,3]
print(sorted([3,1,2]))                    # [1,2,3]
print(str(123))                           # '123'
print(sum([1,2,3]))                       # 6

# T: tuple(), type()
print(tuple([1,2,3]))                     # (1,2,3)
print(type(3.14))                         # <class 'float'>

# V: vars()
print(vars(d))                            # {'x': 100}

# Z: zip()
names = ["Alice", "Bob", "Charlie"]
scores = [90, 70, 88]
print(list(zip(names, scores)))           # [('Alice',90), ('Bob',70), ('Charlie',88)]

# _: __import__()
math_module = __import__("math")
print(math_module.sqrt(16))               # 4.0
```