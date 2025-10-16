
# ⿢ BAR GRAPH: Total Sales by Country
# ============================================================
# Task: Create a bar chart showing total sales for each country.
# Hint:
#   1. Add a 'Sales' column: df['Sales'] = df['Quantity'] * df['Price']
#   2. Group by 'Country' and sum 'Sales'
#   3. Sort values in descending order
#   4. Use plt.bar() to plot
#   5. Display the sales value above each bar
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

df['Sales'] = df['Quantity'] * df['Price']

sales_by_country = df.groupby('Country')['Sales'].sum().sort_values(ascending=False)

plt.barh(sales_by_country.index,sales_by_country.values)

plt.title('Total Sales by Country')
plt.xlabel('Sales')
plt.ylabel('Country')

plt.tight_layout()
plt.show()