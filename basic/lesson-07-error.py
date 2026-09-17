# user input is always a string, even if it looks like a number
user_input = input("Enter your age: ")

try:
    age = int(user_input)
    print(f"In 10 years you'll be {age + 10}")
except ValueError:
    # runs only if int(user_input) fails, e.g. user typed "abc"
    print("That's not a valid number, please enter digits only")


def average_price(prices):
    try:
        return sum(prices) / len(prices)
    except ZeroDivisionError:
        # empty list -> len(prices) is 0
        print("No prices given, can't compute an average")
        return None
    except TypeError:
        # list contains something that isn't a number, e.g. a string
        print("Prices list contains a non-numeric value")
        return None


average_price([10, 20, 30])  # 20.0
average_price([])  # handled, prints message, returns None


def add(a, b=10):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(
            f"add() expects numbers, got {type(a).__name__} and {type(b).__name__}"
        )
    return a + b


try:
    add("Ali")
except TypeError as e:
    print(f"Error: {e}")  # Error: add() expects numbers, got str and int


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    # useful for cleanup, e.g. closing a file or a connection
    print("Done processing")


# --- KeyError and IndexError: the most common runtime errors on collections ---
data = {"name": "Mehdi", "age": 44}

try:
    print(data["email"])  # key doesn't exist in the dict
except KeyError as e:
    print(f"Missing key: {e}")  # e is just the missing key, e.g. 'email'

numbers = [1, 2, 3]
try:
    print(numbers[10])  # index doesn't exist in the list
except IndexError as e:
    print(f"Index error: {e}")


# --- catching multiple exception types in one except ---
def get_item(container, key):
    try:
        return container[key]
    except (KeyError, IndexError, TypeError) as e:
        # one except handles all three -- useful when the fix is the same
        print(f"Couldn't fetch item: {e}")
        return None


print(get_item(data, "email"))  # KeyError
print(get_item(numbers, 10))  # IndexError
print(get_item(None, "x"))  # TypeError -- None isn't subscriptable


# --- try / except / else ---
# "else" runs only if the try block did NOT raise. It keeps the "happy path"
# code separate from the risky code, instead of hiding it inside the try.
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Result: {result}")  # only reached when no exception happened
    finally:
        print("Division attempt finished")  # always runs, error or not


safe_divide(10, 2)
safe_divide(10, 0)


# --- catching Exception as a last-resort fallback ---
# catch specific errors first, then a broad Exception as a safety net for
# anything unexpected. Avoid a bare "except:" though -- it also swallows
# Ctrl+C and interpreter-exit signals, which usually should NOT be caught.
def risky_call(fn):
    try:
        return fn()
    except ValueError as e:
        print(f"Bad value: {e}")
    except Exception as e:  # noqa: BLE001 -- intentional: this IS the fallback lesson
        print(f"Unexpected error ({type(e).__name__}): {e}")


risky_call(lambda: int("abc"))  # caught by the specific ValueError branch
risky_call(lambda: 1 / 0)  # caught by the generic Exception branch


# --- custom exceptions ---
# define your own exception type for errors specific to your program --
# common in real code, e.g. an agent raising its own "tool failed" error
# instead of a generic, unclear one.
class ToolExecutionError(Exception):
    """Raised when a tool call fails inside our (imaginary) agent."""


def call_tool(name):
    if name != "search":
        raise ToolExecutionError(f"Unknown tool: {name}")
    return "search results"


try:
    call_tool("delete_everything")
except ToolExecutionError as e:
    print(f"Tool error: {e}")


# --- re-raising and exception chaining ---
def load_config(path):
    # not using "with" yet (that's its own upcoming lesson) -- this works,
    # but "finally" is needed to guarantee the file gets closed either way
    f = None
    try:
        f = open(path)  # noqa: SIM115 -- deliberately manual, "with" comes later
        return f.read()
    except FileNotFoundError as e:
        # wrap the low-level error in a more meaningful one, but keep the
        # original attached via "from e" so the real cause isn't lost
        raise RuntimeError(f"Could not load config from {path}") from e
    finally:
        if f is not None:
            f.close()


try:
    load_config("does_not_exist.txt")
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")  # the original FileNotFoundError


# --- assert: quick sanity checks, not a substitute for real error handling ---
# meant for catching programmer mistakes during development -- assertions
# can be disabled in production (`python -O`), so never rely on them for
# things like validating user input.
def divide(a, b):
    assert b != 0, "b must not be zero"  # raises AssertionError if False
    return a / b


try:
    divide(10, 0)
except AssertionError as e:
    print(f"Assertion failed: {e}")
