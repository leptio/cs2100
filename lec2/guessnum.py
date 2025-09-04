import random
import math
secret_num: int = random.randint(1,10)
print(secret_num)
guess: int = int(input("my guess: "))
if secret_num == guess:
    print("Guessed")
elif (abs(secret_num-guess)==1):
    print("So close!")
else:
    print("Off")