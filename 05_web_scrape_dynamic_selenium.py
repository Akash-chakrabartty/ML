# 05_web_scrape_dynamic_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Adjust path if needed or use webdriver-manager in future
driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/js/")  # JS-powered page
time.sleep(3)  # wait for JS to load

quotes = []
for q in driver.find_elements(By.CLASS_NAME, "quote"):
    text = q.find_element(By.CLASS_NAME, "text").text
    author = q.find_element(By.CLASS_NAME, "author").text
    quotes.append({"text": text, "author": author})

driver.quit()

df = pd.DataFrame(quotes)
print(df.head())
df.to_csv("quotes_dynamic.csv", index=False)
print("\nSaved to quotes_dynamic.csv")
