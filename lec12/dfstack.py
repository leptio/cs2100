import pandas as pd
df = pd.DataFrame({
    'Person': ['Elephant', 'Cat'],
    'Age': [13, 10]})

new_rows = pd.DataFrame({
    'Person': ['Dog', 'Giraffe'],
    'Age': [3, 6]})

final_df = pd.concat([df, new_rows], ignore_index=True)
print(final_df)
