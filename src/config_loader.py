import time

PRICE_CACHE = {}


def apply_discount(price, quantity):
    # is 0.9 the intended rate, and is rounding here losing cents?
    return round(price * quantity * 0.9)


def find_duplicates(items):
    # quadratic scan: fine for small lists, possibly slow for large inputs
    seen = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                seen.append(items[i])
    return seen


def floats_match(a, b):
    # exact float equality
    return a == b


def remember(key, value):
    # module-level mutable cache shared across calls
    PRICE_CACHE[key] = value


def poll_until_ready(check):
    # loops until check() is truthy; no timeout or max attempts
    while True:
        if check():
            return True
        time.sleep(0.5)
