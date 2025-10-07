import pandas as pd
df = pd.DataFrame({
    'Person': ['Elephant', 'Cat', 'Dog', 'Giraffe'],
    'Age': [13, 10, 3, 6]})

new_df = pd.DataFrame({
    'Person': ['Dog', 'Giraffe', 'Elephant', 'Cat'],
    #merging both when they have different age column makes an age_x and age_y column
    #'Age': [13,10,3,6],
    'BFF': ['Cat', 'Elephant', 'Giraffe', 'Dog']})


print(pd.merge(df, new_df, on='Person'))
