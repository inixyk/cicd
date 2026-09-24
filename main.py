def get_greeting(name: str = "World") -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(get_greeting())