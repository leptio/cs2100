count = int(input('How many numbers?'))
sum: float = 0.0
min:float=float('inf')
max: float=float('-inf')
##accumulator patern
for _ in range(count):
    num = float(input('Please enter a number: '))
    sum += num
    if num < min:
        min = num
    if num > max:
        max = num
print(f'min: {min}\nmax: {max}\navg: {sum/count}')