# 01_csv_excel.py
import pandas as pd

# If you already have data.csv, just read it
# Otherwise, this will create a demo CSV first
data = {
    "name": ["A", "B", "C"],
    "marks": [80, 75, 90]
}
df_demo = pd.DataFrame(data)
df_demo.to_csv("data.csv", index=False)

# Now read CSV
df = pd.read_csv("data.csv")
print("CSV data:")
print(df)

# For Excel:
df.to_excel("data.xlsx", index=False)
df_x = pd.read_excel("data.xlsx")
print("\nExcel data:")
print(df_x)
