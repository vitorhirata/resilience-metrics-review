import pandas as pd
from os.path import exists

dfNames = pd.read_csv('bulk_data/column_names.csv', nrows=5)
column_names = list(dfNames.columns)[:-1]

for search_name in ['review', 'model']:

  df1 = pd.read_csv(f'bulk_data/{search_name}_1.csv', delimiter='\t', header=0, names=column_names)

  delete_columns = []
  for name, values in df1.iteritems():
    if values.isna().sum() == 1000:
      delete_columns.append(name)
  print("Dropped columns", delete_columns)

  df1 = df1.drop(delete_columns, axis=1)

  for i in range(2,13):
    df2 = pd.read_csv(f"bulk_data/{search_name}_{i}.csv", delimiter='\t', header=0, names=column_names)
    df2 = df2.drop(delete_columns, axis=1)
    df1 = df1.append(df2)

    if not exists(f"bulk_data/{search_name}_{i + 1}.csv"): break

  print(f"Final dataframe information {search_name}", df1.info())

  df1.to_csv(f'data/{search_name}.csv')

print("The end.")
