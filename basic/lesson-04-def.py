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
