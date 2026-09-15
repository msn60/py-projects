a = 10
b = 3

print(a + b)  # 13   addition
print(a - b)  # 7    subtraction
print(a * b)  # 30   multiplication
print(a / b)  # 3.333...  true division (always returns float)
print(a // b)  # 3    floor division
print(a % b)  # 1    modulo (remainder) -- what you needed for is_even
print(a**b)  # 1000 exponentiation (a to the power of b)


# a == b  # equality
# a != b  # inequality
# a > b
# a < b
# a >= b
# a <= b

# x = 5
# 0 < x and x < 10    # True
# x < 0 or x > 100     # False
# not (x == 5)         # False

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
