import pandas as pd
df = pd.DataFrame({
    'Person': ['Elephant', 'Cat', 'Frog'],
    'Age': [13,10,3]
})

print(df[df['Age']>5])
print(df[[True, False, True]], "\n")
print(df[lambda dataframe: ['a' in row['Person'] for _, row in dataframe.iterrows()]])

df_write = pd.DataFrame({
    'Title': ["Elephant's Adventures", "Cat's Story", "Frog Life"],
    'Author': ['Elephant', 'Cat', 'Frog'],
    'Year': [13,10,3]
})

result_sort = df_write[lambda dataframe:['e' in row['Title'] for _,row in 
                                 dataframe.iterrows()]].sort_values(by='Year')['Author']

print(result_sort)
