import pandas as pd
df = pd.DataFrame({
    'Person': ['Elephant', 'Cat', 'Frog'],
    'Age': [13,10,3]
})

print(df.sort_values(by='Person'))
