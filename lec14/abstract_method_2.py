from abc import ABC, abstractmethod
#python is duck ryped: "if it quacks like a duck it is a duck"
#can run same function from different objects if it has the function

class Pet(ABC):
    @abstractmethod
    def express_affection(self) -> None:
        pass

class Cat(Pet):
    def express_affection(self) -> None:
        self.make_biscuits()

    def make_biscuits(self) -> None:
        print("Making biscuits")

class Dog(Pet):
    def express_affection(self) -> None:
        self.slobber()

    def slobber(self) -> None:
        print("Slobbering")

#polymorphism: pet variable can be both Cat and Dog
for pet in [Cat(), Dog(), Cat()]:
    pet.express_affection()
