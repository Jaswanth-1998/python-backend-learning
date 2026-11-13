## Core OOP Concepts in Python
### Classes & Objects
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

### Object creation
c1 = Car("Tesla", "Model S")
print(c1.brand)   # Tesla
```

### Method Calls
```python
class Car:
    def start(self):
        print("Car started!")

c1 = Car()
c1.start()   # Method call
```

### Inheritance (Single, Multiple, Multilevel)
```python
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):   # Single Inheritance
    def sound(self):
        print("Bark")

class Puppy(Dog):    # Multilevel Inheritance
    pass

p = Puppy()
p.sound()   # Bark
```

### Overloading (Method Overloading via default args)
```python
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(5))       # 5
print(m.add(5, 10))   # 15
print(m.add(5, 10, 20)) # 35
```

### Overriding
```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):   # Overriding
        print("Child method")

c = Child()
c.show()   # Child method
```

### Data Hiding (Encapsulation)
```python
class Bank:
    def __init__(self):
        self.__balance = 1000   # private variable

    def get_balance(self):
        return self.__balance

b = Bank()
print(b.get_balance())   # 1000
# print(b.__balance) → Error
```

### Operator Overloading
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):   # Overloading +
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3.x, p3.y)   # 6 8
```