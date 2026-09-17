for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

numbers = [10, 20, 30]
for n in numbers:
    print(n)

count = 0
while count < 3:
    print(count)
    count += 1  # += یعنی count = count + 1

fruits = ["apple", "orange", "banana"]
for f in fruits:
    print(f"I like {f}")

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1


# --- break: stop the loop early ---
for n in range(10):
    if n == 5:
        break  # exits the loop immediately, 5 and beyond never print
    print(n)

# find the first even number in a list, then stop looking
values = [3, 7, 9, 4, 11, 8]
for v in values:
    if v % 2 == 0:
        print(f"first even number: {v}")
        break


# --- continue: skip to the next iteration ---
for n in range(10):
    if n % 2 != 0:
        continue  # skip odd numbers, don't print them
    print(n)


# --- range() with start, stop, step ---
print(list(range(2, 10)))  # [2..9]        start=2, stop=10
print(list(range(0, 10, 2)))  # [0,2,4,6,8]   step=2
print(list(range(10, 0, -1)))  # [10..1]       negative step counts down


# --- enumerate(): get index + value together ---
fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

# enumerate can start counting from a different number
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")


# --- zip(): loop over multiple lists in parallel ---
names = ["Ali", "Sara", "Reza"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")


# --- while True + break: the "run until a condition is met" pattern ---
# this shape shows up a lot in agent loops: keep going until told to stop
attempts = 0
while True:
    attempts += 1
    print(f"attempt {attempts}")
    if attempts >= 3:
        print("done")
        break
