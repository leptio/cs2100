from random import random
def thing(n:int,m:int) -> float:
    total:int = sum([int(random()*n) for i in range(m)])
    return total/n

print(thing(10000000,20))