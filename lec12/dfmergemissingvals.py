import pandas as pd
df = pd.DataFrame({
    'Person': ['Elephant', 'Cat', 'Dog', 'Giraffe'],
    'Age': [13, 10, 3, 6]})


new_df = pd.DataFrame({
    'Age': [3, 6, 9, 10],
    'Year': [2022,2019,2016,2015]})

#no data match for age of 13: data is ignored
print(pd.merge(df, new_df))

#outer join takes all data, left join does not discard left, right join does not discard right
print(pd.merge(df, new_df, how='outer'))
