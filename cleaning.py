import pandas as pd

df1Full = pd.read_csv('tmp/1_full.csv', nrows=5)
column_names = list(df1Full.columns)[:-1]

df1 = pd.read_csv('tmp/1.csv', delimiter='\t', header=0, names=column_names)

delete_columns = []
for name, values in df1.iteritems():
  if values.isna().sum() == 1000:
    delete_columns.append(name)
print("Dropped columns", delete_columns)

df1 = df1.drop(delete_columns, axis=1)

for i in range(2,13):
  df2 = pd.read_csv(f"tmp/{i}.csv", delimiter='\t', header=0, names=column_names)
  df2 = df2.drop(delete_columns, axis=1)
  df1 = df1.append(df2)

print("Final dataframe information", df1.info())

df1.to_csv('references.csv')
