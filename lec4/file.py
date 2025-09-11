
class Cat:
    def __init__(self, name:str, human:str):
        self.name = name
        self.human = human
        print(name*3)

mini: Cat = Cat('Mini', 'Rasika')
