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
    return a ** b


OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Power", power),
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
