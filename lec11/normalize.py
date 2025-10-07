from typing import List
x: List[int] = [6,8,9,8,7]
x_min, x_max = min(x), max(x)

x_normalized = [(i-x_min) / (x_max-x_min) for i in x]
print([round(v, 2) for v in x_normalized])