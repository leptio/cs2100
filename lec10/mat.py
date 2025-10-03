import matplotlib.pyplot as plt
from typing import List
import numpy as np

num_categories: int = 10
categories: List[int] = [i for i in range(num_categories)]
values = np.random.rand(num_categories)

plt.bar(categories, values)

plt.title('Days gone without mistaking correlation for causation', fontsize = 16)

plt.show()