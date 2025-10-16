# ⿣ LINE GRAPH: Daily Sales Trend
# ============================================================
# Task: Plot a line graph showing total sales per day.
# Hint:
#   1. Convert 'OrderDate' to datetime: df['OrderDate'] = pd.to_datetime(df['OrderDate'])
#   2. Group by 'OrderDate' and sum 'Sales'
#   3. Use plt.plot() with markers and line style
#   4. Label X-axis, Y-axis, and add a title
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

df['OrderDate'] = pd.to_datetime(df['OrderDate'])

df['Sales'] = df['Quantity'] * df['Price']

daily_sales = df.groupby('OrderDate')['Sales'].sum()

plt.plot(daily_sales.index,daily_sales.values,marker = 'o',linestyle = '-')
plt.title('Daily Sales Trend')
plt.xlabel('OrderDate')
plt.ylabel('Sales')

plt.show()