"""Create Shirt class"""
class Shirt:
    """Class Shirt: 
    contains int "size"
    contains special string constructor"""
    def __init__(self, size:int):
        self.size = size
    def __str__(self) -> str:
        return f'{self.size} is my size. Thank you for printing me!'

def main() -> None:
    six_hundred: int = 600
    subtract_one(six_hundred)
    #prints 600: integers are immutable
    print(six_hundred)

    shirt: Shirt = Shirt(600)
    shrink_shirt(shirt)
    #prints 599: objects are mutable
    print(shirt.size)
    modify_shirt(shirt)
    print(shirt.size)

    print(shirt)

def subtract_one(num:int) -> None:
    """Subtract 1 from an integer"""
    num -=1

def shrink_shirt(shirt: Shirt) -> None:
    """Shrink a shirt's size by 1"""
    shirt.size -= 1

def modify_shirt(shirt: Shirt) -> None:
    """Change a shirt's size to 4"""
    shirt.size = 4

if __name__ == "__main__":
    main()
