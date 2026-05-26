"""Simple command-line calculator."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    if a == 0 and b < 0:
        raise ValueError("Zero cannot be raised to a negative power")
    if a < 0 and not b.is_integer():
        raise ValueError("Negative base requires an integer exponent")
    return a ** b

def square_root(a: float) -> float:
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return a ** 0.5


OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Power", power),
    "6": ("Square Root", square_root),
}


def main() -> None:
    print("=== Calculator ===")
    while True:
        print("\nSelect operation:")
        for key, (name, _) in OPERATIONS.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("Choice: ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice, try again.")
            continue

        try:
            a = float(input("First number: "))
            if choice == "6":
                b = None
            else:
                b = float(input("Second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        name, func = OPERATIONS[choice]
        try:
            result = func(a, b)
            print(f"{name} result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
