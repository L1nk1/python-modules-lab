from lib import add, greet, multiply


def main():
    """Запускає основну логіку програми."""
    print("Sum:", add(5, 3))
    print("Multiplication:", multiply(5, 3))
    print(greet("Nazar"))


if __name__ == "__main__":
    main()
