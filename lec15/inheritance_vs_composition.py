from typing import Set
#inheritance implies "is a" relationship
#example: A square is a rectangle

#composition implies "has a" relationship
#example: A square has four edges

#Composition (SocialMedia * set of users)
class SocialMediaFixed:
    def __init__(self) -> None:
        self.users: Set[str] = set()

    def add_user(self, name:str) -> None:
        self.users.add(name)

class Kitchen:
    def cook(self) -> None:
        print('Cooking...')

class Bedroom:
    def sleep(self) -> None:
        print('Sleeping...')

#Correct: House HAS a kitchen and a bedroom (composition)

class House:
    def __init__(self) -> None:
        self.kitchen = Kitchen()
        self.bedroom = Bedroom()
