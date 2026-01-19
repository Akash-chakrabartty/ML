# 03_rest_api.py
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"
resp = requests.get(url)
resp.raise_for_status()

data = resp.json()
df = pd.DataFrame(data)
print(df.head())
df.to_csv("api_posts.csv", index=False)
print("\nSaved to api_posts.csv")
