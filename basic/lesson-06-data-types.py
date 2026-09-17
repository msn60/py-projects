# Deep dive: data types (numbers, strings, None, collections, casting)

# --- numbers: int vs float ---
a = 10  # int
b = 3.0  # float

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>

# mixing int and float always upgrades the result to float
print(type(a + b))  # <class 'float'>

# big ints are fine, no overflow like in some other languages
big = 2**100
print(big)

# float precision gotcha -- classic example, don't rely on exact equality
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False
print(round(0.1 + 0.2, 2) == 0.3)  # True -- round first when comparing floats


# --- strings: immutable sequences of characters ---
s = "Hello, Mehdi"

print(len(s))
print(s[0])  # 'H'          indexing
print(s[-1])  # 'i'          negative index = from the end
print(s[0:5])  # 'Hello'      slicing [start:stop)
print(s[7:])  # 'Mehdi'
print(s[::-1])  # 'idheM ,olleH'  reversed string

# strings are immutable -- this creates a NEW string, doesn't change s
print(s.upper())
print(s.lower())
print(s.replace("Mehdi", "Ali"))
print(s)  # unchanged

# useful string methods
print("  padded  ".strip())  # 'padded'
print("a,b,c".split(","))  # ['a', 'b', 'c']  # noqa: SIM905
print("-".join(["a", "b", "c"]))  # 'a-b-c'  # noqa: FLY002
print(s.startswith("Hello"))  # True
print("mehdi" in s.lower())  # True -- membership check


# --- bool: truthy / falsy ---
# these all count as False in an if/while check:
falsy_values = [0, 0.0, "", [], {}, set(), None, False]
for v in falsy_values:
    print(v, "->", bool(v))

# everything else is truthy
print(
    bool(1), bool("hi"), bool([0])
)  # True True True (non-empty list, even with a 0 inside)


# --- None: absence of a value ---
result = None
print(result is None)  # use "is", not "==", to check for None
print(type(None))  # <class 'NoneType'>


# --- list: ordered, mutable ---
fruits = ["apple", "banana", "orange"]
fruits.append("kiwi")
fruits.insert(1, "grape")
fruits.remove("banana")
print(fruits)
print(fruits[0], fruits[-1])
fruits.sort()
print(fruits)

# lists are mutable -- careful, this is a shared reference, not a copy
same_list = fruits
same_list.append("mango")
print(fruits)  # also changed! same_list and fruits point to the same list

copy_list = fruits.copy()
copy_list.append("only in copy")
print(fruits)  # unaffected
print(copy_list)


# --- tuple: ordered, immutable ---
point = (10, 20)
print(point[0], point[1])

# point[0] = 99  # TypeError -- tuples can't be changed after creation

x, y = point  # unpacking
print(f"x={x}, y={y}")


# --- set: unordered, unique items ---
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)
print(unique)  # {1, 2, 3} -- duplicates removed, order not guaranteed

a_set = {1, 2, 3}
b_set = {2, 3, 4}
print(a_set | b_set)  # union -> {1, 2, 3, 4}
print(a_set & b_set)  # intersection -> {2, 3}
print(a_set - b_set)  # difference -> {1}


# --- dict: key-value pairs ---
person = {"name": "Mehdi", "age": 44}
print(person["name"])
person["city"] = "Tehran"  # add a new key
person["age"] = 45  # update an existing key
print(person)

print(person.get("job"))  # None -- no error, unlike person["job"]
print(person.get("job", "unknown"))  # 'unknown' -- default value

for key, value in person.items():
    print(f"{key}: {value}")

print(list(person.keys()))
print(list(person.values()))


# --- checking and converting types ---
value = "42"
print(type(value))  # <class 'str'>
print(isinstance(value, str))  # True -- preferred over type() == for checks

n = int(value)  # str -> int
f = float(value)  # str -> float
s2 = str(n)  # int -> str
print(n, f, s2, type(n), type(f), type(s2))

# not every conversion is safe
try:
    int("not a number")
except ValueError as e:
    print("conversion failed:", e)


# these all behave as "False" in an if statement
bool(0)  # False
bool("")  # False (empty string)
bool([])  # False (empty list)
bool(None)  # False

# everything else is "True"
bool(5)  # True
bool("hi")  # True

name = ""
if name:  # instead of: if name != ""
    print("has a name")
else:
    print("empty")
