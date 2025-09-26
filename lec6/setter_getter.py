class Person:
    def __init__(self, age: int):
        self._age = age
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age


mini: Person = Person(10)
mini.age = 11
print(mini.age) # 11

my_long_tuple: tuple[int, ...] = tuple([-i for i in range(5)])
my_long_tuple = tuple(sorted(my_long_tuple))
print(my_long_tuple)

