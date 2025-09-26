"""Initializes class print_cat"""
#stack is first-in, last-out
#main() first (at the bottom) then print_cat() (at the top) of the stack

def print_cat(name: str, age: int) -> None:
    """Prints a cat's info."""

    description: str = f"Cat's name is {name}, and age is {age}"
    print(description)

def main() -> None:
    """Runs print_cat with arguments."""
    cat_name: str = "Cool Cat"
    cat_age: int = 35

    #set breakpoint here to step into print_cat()
    print_cat(cat_name, cat_age)

if __name__ == "__main__":
    main()
