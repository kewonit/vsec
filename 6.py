from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_Nobel_Peace_Prize_winners'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
data = []

for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) >= 3:
        year = cols[0].text.strip()
        name = cols[1].text.strip()
        country = cols[2].text.strip()
        data.append([year, name, country])

df = pd.DataFrame(data, columns=['Year', 'Name', 'Country'])

print(df.head())
print(df.describe())
print(df['Country'].value_counts().head())
print(df.sort_values('Year', ascending=False).head())
print(df[df['Year'] > '2015'])