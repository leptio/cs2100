#__len__ is len() for a class
#__contains__ sees if something contains in something

class Cat():
    def __init__(self) -> None:
        self.bigstring = "food"
    def __len__(self) -> int:
        return 900
    def __contains__(self, req: str) -> bool:
        return(req in self.bigstring)
    
print(len(Cat()))
print("food" in Cat())