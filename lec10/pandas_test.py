import pandas as pd
#series: one-dimensional labelled arrays of any data type
#dataframes: two dimensional labelled arrays of any data type
#time series: index as data frames
#panels: three-dimensional container of data
df = pd.DataFrame(
    {'Person': ['Elephant', 'Cat'],
    'Age': [13, 10]}
)

print(df)

for index, row in df.iterrows():
    print(f"{row['Person']}'s age is {row['Age']}")

new_rows: pd.DataFrame = pd.DataFrame({
    'Person': ['Dog', 'Giraffe'],
    'Age': [3,6]
})

#concatenate new rows into dataframe
df = pd.concat([df, new_rows], ignore_index=True)

#add extra column
df['BFF'] = ["Cat", "Giraffe", "Cat", "Elephant"]

print(df)
