def greet(name):
    return f"Hello, {name}"


result = greet("Ali")
print(result)


# مقدار پیش‌فرض
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


greet("Ali")  # "Hello, Ali"
greet("Ali", "Hi")  # "Hi, Ali"
greet("Ali", greeting="Salam")  # با نام پارامتر هم میشه صداش زد


# چند تا مقدار برگردوندن (در واقع یه tuple برمی‌گرده)
def min_max(numbers):
    return min(numbers), max(numbers)


low, high = min_max([3, 1, 4, 1, 5])
print(f"low:{low}, hight:{high}")


def is_even(n):
    return n % 2 == 0


result = is_even(10)
print(result)


def stats(numbers):
    average = sum(numbers) / len(numbers)
    return min(numbers), max(numbers), average


low, high, average = stats([3, 1, 4, 1, 5])
print(f"low:{low}, hight:{high}, avg:{average}")


def add(a, b=10):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None  # or raise an error later when we cover exceptions
    return a + b


print(add(30))
print(add(20, 50))
print(add("Ali"))


# --- docstrings: the standard way to document a function ---
def area_of_circle(radius):
    """Return the area of a circle given its radius."""
    return 3.14159 * radius**2


print(area_of_circle(2))
print(area_of_circle.__doc__)  # docstrings are readable at runtime too


# --- mutable default argument gotcha ---
# DON'T do this -- the same list is reused across every call
def add_item_wrong(item, items=[]):  # noqa: B006 -- intentional, this is the gotcha
    items.append(item)
    return items


print(add_item_wrong("a"))  # ['a']
print(add_item_wrong("b"))  # ['a', 'b']  <- surprise! same list as before


# correct way: default to None, create a new list inside the function
def add_item_right(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item_right("a"))  # ['a']
print(add_item_right("b"))  # ['b']  <- fresh list each time


# --- scope: local vs global ---
counter = 0  # global variable


def increment_local():
    counter = 100  # this creates a NEW local variable, doesn't touch the global one
    counter += 1
    return counter


print(increment_local())  # 101
print(counter)  # still 0 -- untouched


def increment_global():
    global counter  # explicitly say we mean the global variable
    counter += 1
    return counter


print(increment_global())  # 1
print(counter)  # 1 -- actually changed


# --- lambda: small anonymous functions ---
square = lambda n: n**2  # same as: def square(n): return n**2
print(square(5))

# lambdas are mostly used inline, e.g. as a sort key
people = [("Ali", 25), ("Sara", 19), ("Reza", 31)]
people.sort(key=lambda person: person[1])  # sort by age
print(people)


# --- functions as values: pass them around like any other variable ---
def loud(text):
    return text.upper() + "!"


def quiet(text):
    return text.lower() + "..."


def shout_with(formatter, text):
    return formatter(text)  # formatter is just a function passed in


print(shout_with(loud, "hello"))
print(shout_with(quiet, "HELLO"))


def make_multiplier(factor):
    """Return a new function that multiplies its input by `factor`."""

    def multiplier(n):
        return n * factor

    return multiplier  # returning a function, not calling it


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))  # 20
print(triple(10))  # 30


# --- recursion: a function that calls itself ---
def factorial(n):
    if n <= 1:  # base case -- stops the recursion
        return 1
    return n * factorial(n - 1)  # recursive case


print(factorial(5))  # 120


def countdown_recursive(n):
    if n <= 0:
        print("liftoff!")
        return
    print(n)
    countdown_recursive(n - 1)


countdown_recursive(3)
