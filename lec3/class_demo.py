"""Defines and uses class Pet and Cat, which define household objects"""
import unittest

class Pet:
    """Represents a household pet"""
    def __init__(self, pet_name:str, owner_name: str, animal:str):
        self.name: str = pet_name
        self.owner: str = owner_name
        if animal == "cat":
            self.sound = "meow"
        elif animal == "dog":
            self.sound = "bark"
        else:
            self.sound = "hello"
    def make_sound(self) -> str:
        """Returns the sound of the pet"""
        return self.sound

class Cat:
    """Represents a household cat"""
    def __init__(self, name:str):
        self.name = name
        self.age = 0

    def birthday(self) -> None:
        """function birthday: ages up cat by 1"""
        self.age += 1

    def make_sound(self) -> str:
        """returns 'meow' once for each year in the cat's age"""
        return ("meow " * self.age).strip()

class TestCat(unittest.TestCase):
    """Tests Cat behavior."""    
    def setUp(self) -> None:
        self.cat = Cat('Mini')

    def test_initial_sound_empty(self) -> None:
        """ensure that there is no sound output from age 0 cat"""
        self.assertEqual('', self.cat.make_sound())

    def test_after_three_years(self) -> None:
        """ensure that there are 3 meows outputted from age 3 cat"""
        for _ in range(3):
            self.cat.birthday()
        self.assertEqual('meow meow meow', self.cat.make_sound())

new_pet: Pet = Pet("The Dog", "Me", "dog")

print(new_pet.make_sound())

mini: Cat = Cat("Mini")

for year in range(3):
    mini.birthday()

print(mini.make_sound() + Cat('Mega').make_sound())

if __name__ == "__main__":
    unittest.main()
