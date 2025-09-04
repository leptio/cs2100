#swap variables
#can also perform with x,y=y,x
x:int = 3
y:int = 4
temp: int=x
x=y 
y=temp

print(x)
print(y)

print("I am so excited"+"!"*3)

cats:int = 4
print(f"There are {cats} cats in this room.")

num:float = 2.5
print(type(4/2))

my_decision: bool = True
my_decision = not my_decision
your_decision:bool = 4<6
print(my_decision and your_decision)
print(my_decision or your_decision)
