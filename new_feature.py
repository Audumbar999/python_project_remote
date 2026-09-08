def add(a, b):
    return a + b


def is_even(number):
    """Return True if the number is even."""
    return number % 2 == 0


if __name__ == "__main__":
    print("10 + 5 =", add(10, 5))
    print("Is 10 even?", is_even(10))
