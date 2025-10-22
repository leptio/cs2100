#class variable shared across all instances, accessed with class name
#instance variables are specific to an object, accessed with self

#class variable:
class Counter:
    count: int = 0

    def __init__(self) -> None:
        Counter.count += 1

ct1 = Counter()
print(ct1.count)

ct2 = Counter()
print(ct1.count)
print(ct2.count)

for i in range(10):
    Counter()

print(ct1.count)

Counter.count+=10

print(ct1.count)
