import pandas as pd
from os.path import exists

dfNames = pd.read_csv('bulk_data/column_names.csv', nrows=5)
column_names = list(dfNames.columns)[:-1] # remove last column as it is not present is CSV

delete_columns = [
  'Book Authors', 'Book Editors', 'Book Group Authors', 'Book Author Full Names',
  'Book Series Title', 'Book Series Subtitle', 'Book DOI', 'DOI Link', 'Open Access Designations'
]

for search_name in ['review', 'model']:
  df1 = pd.read_csv(f'bulk_data/{search_name}_wos_1.csv', delimiter='\t', header=0, names=column_names)
  df1 = df1.drop(delete_columns, axis=1)

  for i in range(2,13):
    df2 = pd.read_csv(f"bulk_data/{search_name}_wos_{i}.csv", delimiter='\t', header=0, names=column_names)
    df2 = df2.drop(delete_columns, axis=1)
    df1 = pd.concat([df1, df2])

    if not exists(f"bulk_data/{search_name}_wos_{i + 1}.csv"): break

  print(f"Final dataframe size for {search_name}: {len(df1)}")
  print(df1.info())

  df1.index.name = 'index'
  df1.to_csv(f'data/{search_name}_wos.csv')

print("The end.")
