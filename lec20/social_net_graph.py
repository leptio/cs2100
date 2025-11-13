class Person:
    def __init__(self, person_id: str):
        self.id = person_id
        self.friends: set[Person] = set()
    
    def __str__(self) -> str:
        return self.id
    
class SocialGraph:
    def __init__(self, location: str) -> None:
        self.people: set[Person] = set()
        self.location = location
    
    def __str__(self) -> str:
        return f'People in {self.location}: {self.people}'