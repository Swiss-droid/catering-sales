import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("catering_bakery_monthly.csv")
print(df)
print()

print(df.describe())
print()

print(df.info())
print()

print("Total Revenue (ZAR)")
print(f"The total revenue made this month is: {df["Total_Revenue_ZAR"].sum()}")
print(f"The average revenue this month is: {round(df["Total_Revenue_ZAR"].mean(), 2)}")
print()

print(f"The total celebration cakes sold this month is: {df["Celebration_Cakes"].sum()}")
print(f"The total vetkoek boxes sold this month is: {df["Vetkoek_Boxes_Sold"].sum()}")
print(f"The total flour in kg used this month is: {round(df["Flour_Used_Kg"].sum(), 2)}")
print(f"The total meat in kg used this month is: {df["Meat_Used_Kg"].sum()}")
print(f"The total packaging boxes used this month is: {df["Packaging_Boxes_Used"].sum()}")
print()


# Plotting the graph
x = df["Day"]
y = df["Total_Revenue_ZAR"]
plt.barh(df["Day"], df["Total_Revenue_ZAR"], color = "purple")
plt.xlabel("Revenue")
plt.ylabel("Day")
plt.title("Daily Revenue for the Month")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()
