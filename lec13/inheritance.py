#subclass is a more specific version of superclass (subclass = child class, superclass = parent class)
#subclass inherits all methods and attributes
#can add more methods and attributes specific to itself
#when declaring subclass, put the superclass's name in parentheses

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv[Liskov Substitution Principle]vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#objects of a superclass can be replaced with objects of its subclass without altering expected functionality
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class Cat():
    def __init__(self, fur: str, claws: str):
        self.claws = claws
        self.fur = fur
        self.food: list[str] = ['tuna', 'chicken', 'zebra']
    
    def eat(self, food: str) -> None:
        if food in self.food:
            print(f'Eating {food}')

class Lion(Cat):
    def roar(self, noise: str) -> None:
        print(f"The {self.fur} lion roars {noise}!")

    def eat(self, food: str) -> None:
        self.food+={'zebra'}
        super().eat(food)

new_lion: Lion = Lion("black", "sharp")
new_lion.roar("very loudly")
new_lion.eat("zebra")
new_cat: Cat = Cat("white", "sharp")
new_cat.eat("tuna")
