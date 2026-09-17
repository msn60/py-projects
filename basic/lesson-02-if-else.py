age = 20

if age >= 18:
    print("adult")
elif age > 12:
    print("teen")
else:
    print("child")

score = 56
if score >= 90:
    print("The score range is A")
elif score >= 70:
    print("The score range is B")
elif score >= 50:
    print("The score range is C")
else:
    print("The score range is F")


# --- ternary / conditional expression ---
# a compact if/else that returns a value -- very common idiom
status = "adult" if age >= 18 else "minor"
print(status)

label = "even" if score % 2 == 0 else "odd"
print(label)


# --- nested if ---
has_id = True
if age >= 18:
    if has_id:
        print("can enter")
    else:
        print("need ID")
else:
    print("too young")


# --- membership check inside a condition ---
allowed_roles = ["admin", "editor", "viewer"]
role = "editor"

if role in allowed_roles:
    print(f"{role} is allowed")
else:
    print(f"{role} is NOT allowed")

# combined with not
if "banned" not in allowed_roles:
    print("banned role is not in the allowed list")
