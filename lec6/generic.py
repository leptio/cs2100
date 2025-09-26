"""Creates function that simulates stack behavior"""
from typing import List, TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    """Function that simulates stack behavior"""
    def __init__(self) -> None:
        self.items: List[T] = []

    def push (self, item: T) -> None:
        """Pushes an item to the list"""
        self.items.append(item)

    def pop(self) -> T:
        """Pops an item from the list"""
        return self.items.pop()

    def is_empty(self) -> bool:
        """Returns a bool that states whether or not the stack is empty"""
        return not self.items

my_stack: Stack[int] = Stack()
my_stack.push(4)
print(my_stack.pop())
