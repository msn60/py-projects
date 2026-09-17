print("hello gholam")

name = "Mehdi"  # str (رشته)
nameAndFamily = "Mehdi Soltani Neshan"
age = 44  # int (عدد صحیح)
height = 1.77  # float (اعشاری)
is_ready = True  # bool (درست/غلط)

print(name, age)
print(f"{name} is {age} years old")  # f-string، رایج‌ترین روش چاپ ترکیبی
print(f"Name:{name}, Age:{age}, Height:{height}, is_ready:{is_ready}")


# --- multiple assignment ---
x, y, z = 1, 2, 3  # assign three values in one line
print(x, y, z)

a = b = 0  # same value to multiple names at once
print(a, b)

x, y = y, x  # swap without a temp variable
print(x, y)


# --- f-string format specs ---
price = 1234.5
pi = 3.14159265

print(f"{pi:.2f}")  # '3.14'        -- 2 decimal places
print(f"{price:,.2f}")  # '1,234.50'    -- thousands separator + 2 decimals
print(f"{age:5d}")  # '   44'       -- right-aligned in a 5-char field
print(f"{name:<10}|")  # 'Mehdi     |' -- left-aligned, padded to 10 chars
print(f"{nameAndFamily:<10}|")  # 'Mehdi     |' -- left-aligned, padded to 10 chars
print(f"{name:>10}|")  # '     Mehdi|' -- right-aligned, padded to 10 chars
