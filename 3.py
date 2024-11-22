import pandas as pd

data = {
    'name': ['Kew1', 'Kew2', 'Kew3', 'Kew4'],
    'age': [18, 19, 20, 21],
    'grade': [35, 53, 78, 95]
}

df = pd.DataFrame(data)

print(df)
print(df['name'])
print(df[df['grade'] > 80])
print(df.sort_values('age'))