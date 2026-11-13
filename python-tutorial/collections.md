## List
```python
print([10, 20, 30])
print([1, "Kalidas", 3.5, True])
print(type([]))   # <class 'list'>
print(list(("apple", "banana", "cherry"))) # ['apple', 'banana', 'cherry']

nums = [10, 20, 30, 40, 50]
print(nums[0])     # 10
print(nums[-1])    # 40 (last element)
nums[1] = 99 # update
print(len([10, 20, 30]))   # 3 length
print([1, 2] + [3, 4])     # [1, 2, 3, 4] Concatenation
print(20 in [10, 20, 30]) # true Membership in (true/false)
print(min(nums)) 
print(max(nums))  
print(sum(nums))

# Slicing
list[start : end : step]

print(a[1:4])    # [20, 30, 40]
print(a[:3])     # [10, 20, 30]
print(a[2:])     # [30, 40, 50]
print(a[-3:])    # [30, 40, 50]
print(a[::2])    # [10, 30, 50]
print(a[::-1])   # [50, 40, 30, 20, 10] (reverse)

# comprehension
squares = [x*x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

## List Methods
```python
lst = [10, 20, 30, 20, 40]
print("Original List:", lst)

# 1) append() -> adds one element at the end
lst.append(50)
print("After append(50):", lst)

# 2) extend() -> adds multiple elements at the end
lst.extend([60, 70])
print("After extend([60, 70]):", lst)

# 3) insert() -> inserts at a specific index
lst.insert(1, 15)
print("After insert(1, 15):", lst)

# 4) remove() -> removes first occurrence of a value
lst.remove(20)
print("After remove(20):", lst)

# 5) pop() -> removes by index (default last) and returns removed element
removed_last = lst.pop()
print("pop() removed:", removed_last, "List:", lst)

removed_index = lst.pop(2)
print("pop(2) removed:", removed_index, "List:", lst)

# 6) clear() -> removes all elements
temp = lst.copy()
temp.clear()
print("After clear():", temp) # After clear(): []

# 7) index() -> returns first index of the value
print("Index of 20:", lst.index(20)) # 2

# 8) count() -> counts occurrences
print("Count of 20:", lst.count(20)) # 1

# 9) sort() -> sorts the list in ascending order (in-place)
nums = [4, 1, 9, 2, 7]
print("\nNew nums:", nums) # New nums: [4, 1, 9, 2, 7]
nums.sort()
print("After sort():", nums) # After sort(): [1, 2, 4, 7, 9]

# sort(reverse=True) -> descending
nums.sort(reverse=True)
print("After sort(reverse=True):", nums) # After sort(reverse=True): [9, 7, 4, 2, 1]

# 10) reverse() -> reverses the list (in-place)
nums.reverse()
print("After reverse():", nums) # After reverse(): [1, 2, 4, 7, 9]

# 11) copy() -> returns a shallow copy
copy_list = nums.copy()
print("copy() result:", copy_list) # copy() result: [1, 2, 4, 7, 9]

# 12) (Bonus) Difference: append vs extend
a = [1, 2]
a.append([3, 4])
print("\nappend([3,4]) =>", a)   # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print("extend([3,4]) =>", b)    # [1, 2, 3, 4]
```

## Tuple
```python
t = (1, 2, 3, 2, "apple") # (1, 2, 3, 2, 'apple')
print(type(t)) # <class 'tuple'>

sample = (
    10,                 # int
    9.5,                # float
    2+3j,               # complex
    "Kalidas",          # str
    [1, 2, 3],          # list
    (10, 20),           # tuple
    {"name": "K"},      # dict
    {1, 2, 3},          # set
    True,               # bool
    b"hi",              # bytes
    bytearray(3),       # bytearray
    memoryview(bytes(2)), # memoryview
    None                # NoneType
) # (10, 9.5, (2+3j), 'Kalidas', [1, 2, 3], (10, 20), {'name': 'K'}, {1, 2, 3}, True, b'hi', bytearray(b'\x00\x00\x00'), <memory at 0x7e9f93a45d80>, None)

print(t)

print("count:", t.count(2))        # count: 2
print("index:", t.index("apple"))  # index: 4
print("access:", t[1])             # access: 2
print("slice:", t[1:4])            # slice: (2, 3, 2)

print("length:", len(t))           # length: 5
print("check:", 3 in t)            # check: True

print("loop:")
for x in t:
    print(x)

```

## Set
```python
s = {1, 2, 3, 3}
print(s)   # {1, 2, 3}
print(type(s)) # <class 'set'>

s2 = {3, 4, 5, 6}

s.add(7)                     # {1,2,3,4,7}
s.update([8, 9])             # {1,2,3,4,7,8,9}

s.remove(1)                  # {2,3,4,7,8,9}
s.discard(10)                # no change
popped = s.pop()             # random removed
copy_set = s.copy()          # copy created

print("copy:", copy_set)  # copy: {3, 4, 7, 8, 9}
print("popped:", popped) # popped: 2
print("union:", s.union(s2))                      # union: {all unique} {3, 4, 5, 6, 7, 8, 9}
print("intersection:", s.intersection(s2))        # intersection: common {3, 4}
print("difference:", s.difference(s2))            # difference: s - s2 {8, 9, 7}
print("symmetric_difference:", s.symmetric_difference(s2)) # {5, 6, 7, 8, 9}

print("subset:", {3,4}.issubset(s))               # True
print("superset:", s.issuperset({3}))             # True
print("disjoint:", s.isdisjoint({100}))           # True

s.intersection_update({3,4,7})
s.difference_update({7})
s.symmetric_difference_update({4,10})

print("length:", len(s))                          # length 2
print("contains 3:", 3 in s)                      # check item 3

temp = {1,2}
temp.clear()                                      # {}

print("final s:", s)  # final s: {10, 3}

l = list(s)
print(l, l[0])  # [10, 3] 10

# 1️⃣ Loop access
for x in s:
    print(x)

# Duplicates not allowed
print(set(("CSK","RCB",True,1))) #{True?False, 'RCB', 'CSK'}
print(set(("CSK","RCB",1, True))) #{'RCB',1/0, 'CSK'}
```

## Dictionary
```python
d1 = {"a": 1, "b": 2} # {"a": 1, "b": 2}
d2 = dict(x=10, y=20) # {"x": 10, "y": 20}                 
d3 = dict([("a", 1), ("b", 2)]) # {"a": 1, "b": 2} 

print(type(d1)) #<class 'dict'>
print("=== 1) BASICS: create, access, update ===")
person = {"name": "Kalidas", "role": "SSE", "city": "Chennai"}
print("person:", person)  #person: {'name': 'Kalidas', 'role': 'SSE', 'city': 'Chennai'}

# Access
print("name (index):", person["name"])          # Kalidas may raise KeyError if missing
print("age (get):", person.get("age"))          # None safe: returns None
print("age (get default):", person.get("age", 25)) # 25

# Add / Update
person["age"] = 26                             # add
person["role"] = "Senior Software Engineer"     # updateb
print("after add/update:", person) #{'name': 'Kalidas', 'role': 'Senior Software Engineer', 'city': 'Chennai', 'age': 26}

print("\n=== 2) OPERATIONS: membership, iterate, length ===")
print("'name' in person?", "name" in person)    # True checks keys
print("'Kalidas' in person?", "Kalidas" in person) #False

print("len(person):", len(person)) #4

print("Iterate keys:")
for k in person:
    print(" ", k)

print("Iterate values:")
for v in person.values():
    print(" ", v)

print("Iterate key-value pairs:")
for k, v in person.items():
    print(f"  {k} -> {v}")

print("\n=== 3) METHODS: update, pop, popitem, setdefault, copy, clear ===")

# update()
extra = {"company": "Microsoft", "city": "Chennai"}  # city overwritten
person.update(extra)
print("after update():", person) #{'name': 'Kalidas', 'role': 'Senior Software Engineer', 'city': 'Chennai', 'age': 26, 'company': 'Microsoft'}

# pop()
removed_age = person.pop("age")
print("pop('age') returned:", removed_age) #26
print("after pop('age'):", person) #{'name': 'Kalidas', 'role': 'Senior Software Engineer', 'city': 'Chennai', 'company': 'Microsoft'}

# setdefault(): set only if key is missing
person.setdefault("skills", [])
person["skills"].extend(["Python", "SQL"])
print("after setdefault('skills') + extend:", person) #  {'name': 'Kalidas', 'role': 'Senior Software Engineer', 'city': 'Chennai', 'company': 'Microsoft', 'skills': ['Python', 'SQL']}

# popitem(): removes last inserted (in Python 3.7+ insertion order is preserved)
last_kv = person.popitem()
print("popitem() returned:", last_kv) # ('skills', ['Python', 'SQL'])
print("after popitem():", person) # {'name': 'Kalidas', 'role': 'Senior Software Engineer', 'city': 'Chennai', 'company': 'Microsoft'}

# copy() (shallow copy)
person_copy = person.copy()
print("copy:", person_copy) # {'name': 'Kalidas', 'role': 'Senior Software Engineer', 'city': 'Chennai', 'company': 'Microsoft'}

# clear()
temp = {"a": 1}
temp.clear()
print("after clear():", temp) # {}

print("\n=== 4) MERGE DICTS (3.9+): | and |=, plus unpacking ** ===")
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

merged_pipe = a | b     # b overwrites conflicts
print("a | b:", merged_pipe) # {'x': 1, 'y': 99, 'z': 3}

a |= b                  # in-place merge
print("a after a |= b:", a) #  {'x': 1, 'y': 99, 'z': 3}

merged_unpack = {**{"p": 10}, **{"q": 20}}
print("{**d1, **d2}:", merged_unpack) # {'p': 10, 'q': 20}

print("\n=== 5) COMPREHENSIONS: build dict, filter, invert ===")
# Squares
squares = {x: x * x for x in range(1, 6)}
print("squares:", squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition (only even)
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print("even_squares:", even_squares) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Invert mapping (keys/values swapped) - beware duplicates overwrite
d = {"a": 1, "b": 2}
inv = {v: k for k, v in d.items()}
print("invert d:", inv) # {1: 'a', 2: 'b'}

print("\n=== 6) COMMON INTERVIEW TASK: frequency count using dict ===")
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("freq:", freq) # {'b': 1, 'a': 3, 'n': 2}

print("\n=== 7) NESTED DICTS ===")
emp = {"name": "Asha", "skills": {"python": "good", "sql": "mid"}}
print("nested:", emp) # {'name': 'Asha', 'skills': {'python': 'good', 'sql': 'mid'}}
print("emp['skills']['python']:", emp["skills"]["python"]) # good
```