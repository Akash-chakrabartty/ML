# 04_web_scrape_static.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

books = []
for b in soup.select("article.product_pod"):
    title = b.h3.a["title"]
    price = b.select_one(".price_color").text
    books.append({"title": title, "price": price})

df = pd.DataFrame(books)
print(df.head())
df.to_csv("books_static.csv", index=False)
print("\nSaved to books_static.csv")
