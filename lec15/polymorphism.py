from abc import ABC, abstractmethod
from typing import List

class Vehicle(ABC):
    def __init__(self, mpg: int):
        self.fuel_used: float = 0.0
        self.mpg = mpg
    
    def move(self, distance: int) -> None:
        self.fuel_used += (distance / self.mpg)

    def get_fuel(self) -> float:
        return self.fuel_used

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__(26)

class Motorcycle(Vehicle):
    def __init__(self) -> None:
        super().__init__(55)

class Truck(Vehicle):
    def __init__(self) -> None:
        super().__init__(7)

def get_total_gas(fleet: List[Vehicle]) -> float:
    return sum(veh.get_fuel() for veh in fleet)

fleet: List[Vehicle] = [Car(), Car(), Truck(), Motorcycle(), Motorcycle(), Motorcycle(), Motorcycle()]

for veh in fleet: veh.move(10)

print(get_total_gas(fleet))