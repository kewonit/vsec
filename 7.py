import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20
}

response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20")
data = response.json()
df = pd.DataFrame(data)
print(df)

print("Top 5 cryptocurrencies by price:")
print(df[["name", "current_price"]].head())

print("\nAverage price of top 20 cryptocurrencies:")
print(df["current_price"].mean())

print("\nHighest market cap cryptocurrency:")
print(df.loc[df["market_cap"].idxmax()]["name"])

print("\nSorting by volume:")
print(df[["name", "total_volume"]].sort_values("total_volume", ascending=False).head())

print("\nTotal market cap of all coins:")
print(df["market_cap"].sum())