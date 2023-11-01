import pandas as pd

df1 = pd.read_csv('../dataset/Route Latlong.csv')
df1 = df1.drop(['Unnamed: 3', 'Unnamed: 4', 'Unnamed: 6'], axis=1)
df1.columns = ['direction', 'stop-seq', 'stop-name', 'stop-number', 'latitude', 'longitude']
print(df1.columns)
print(df1.head())


df1 = df1.query('direction == "UP"')
# df1.dropna(subset=['direction'], axis=0)
df1 = df1.apply(lambda x: x.str.lower())
df1 = df1.drop_duplicates(subset=['stop-name'])
df1['stop-name'] = df1['stop-name'].str.replace('(e)', 'east')
df1['stop-name'] = df1['stop-name'].str.replace('(w)', 'west')
df1['stop-name'] = df1['stop-name'].str.replace('(', '')
df1['stop-name'] = df1['stop-name'].str.replace(')', '')
df1['stop-name'] = df1['stop-name'].str.replace(' or ', ' ')

print(df1.head())
print(len(df1))


df1 = df1.reset_index(drop=True)

df1 = df1.drop(['direction', 'stop-seq'], axis=1)
print(df1.head())


df2 = pd.read_csv('../dataset/700.csv')
df2 = df2.iloc[:, :5]
df2 = df2.query('route_name == "7006"')
df2 = df2.apply(lambda x: x.str.lower())
print(df2.columns)
print(len(df2))



mergedFrame = pd.merge(df2, df1, right_on='stop-name', left_on='from_stop_name')
print(len(mergedFrame))
# print(mergedFrame[0:60])




