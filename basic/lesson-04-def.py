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
