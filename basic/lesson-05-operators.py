a = 10
b = 3

print(a + b)  # 13   addition
print(a - b)  # 7    subtraction
print(a * b)  # 30   multiplication
print(a / b)  # 3.333...  true division (always returns float)
print(a // b)  # 3    floor division
print(a % b)  # 1    modulo (remainder) -- what you needed for is_even
print(a**b)  # 1000 exponentiation (a to the power of b)


# --- comparison operators (actually run, not just commented) ---
print(a == b)  # False  -- equality
print(a != b)  # True   -- inequality
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False


# --- logical operators ---
x = 5
print(0 < x and x < 10)  # noqa: PLR1716 -- True, both conditions must be true
print(x < 0 or x > 100)  # False -- neither condition is true
print(not (x == 5))  # noqa: SIM201 -- False, flips True to False

count = 0
count += 10  # same as count = count + 1
print(count)
count -= 3
print(count)
count *= 2
print(count)
count /= 3
print(count)


# check if a number is between 10 and 20
n = 15

if n >= 10 and n <= 20:
    print(f"{n} is between 10 and 20")
else:
    print(f"{n} is NOT between 10 and 20")

# or
if 10 <= n <= 20:
    print(f"{n} is between 10 and 20")


def is_even(n):
    return n % 2 == 0


# test with an even number
print(is_even(8))  # True

# test with an odd number
print(is_even(7))  # False


# --- membership operators: in / not in ---
allowed = [10, 20, 30]
print(15 in allowed)  # False
print(20 in allowed)  # True
print(15 not in allowed)  # True


# --- identity operators: is / is not ---
# "==" checks equal VALUE, "is" checks it's the SAME object in memory
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # True  -- same values
print(list1 is list2)  # False -- different objects in memory
print(list1 is list3)  # True  -- list3 points to the exact same object

# "is" is the correct way to check for None (not "==")
value = None
print(value is None)  # True
print(value == None)  # also True, but "is" is the idiomatic/preferred way


# --- string concatenation and repetition ---
first = "Py"
second = "thon"
print(first + second)  # 'Python'  -- + joins strings
print("ha" * 3)  # 'hahaha'  -- * repeats a string
print("-" * 20)  # a quick divider line, common in printed output
