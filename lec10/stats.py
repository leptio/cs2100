import pandas as pd
import numpy as np
#pearson correlation coefficient

df = pd.DataFrame(
    {'Person': ["Elephant", "Cat", "Dog"],
     'Age': [15,4,9],
     'Height': [16,4,8]}
)

print(np.corrcoef(df['Age'], df['Height']))
print(df.corr(numeric_only=True))