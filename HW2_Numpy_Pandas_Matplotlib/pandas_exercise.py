#The vgsales.csv contains sale data of more than 16000 games sorted by rank.
import pandas as pd

df = pd.read_csv("vgsales.csv")
print(f"File contains {df.shape[0]} games") 

print("Top 10 SNES games:")
print(df[df.Platform == "SNES"][:10].Name)

salesvolume = df[df.Year == 1996].Global_Sales.sum()
print(f"Global sales in 1996: {salesvolume}")

df["Global_Sales_excl_Europe"] = df.apply(lambda x: x.Global_Sales - x.EU_Sales, axis=1)
print(df["Global_Sales_excl_Europe"])

newdf = df[["Name", "Global_Sales"]].groupby("Name").sum().sort_values(by=['Global_Sales'], ascending=False)
print(newdf)

top5_in_newdf = newdf[:5]
print(f"Top 5 in new df: {top5_in_newdf}")