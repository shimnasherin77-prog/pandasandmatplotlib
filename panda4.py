
# ⿤ LINE GRAPH: Category-wise Average Price
# ============================================================
# Task: Draw a line chart showing the average product price per category.
# Hint:
#   1. Group by 'Category' and calculate mean of 'Price'
#   2. Use plt.plot() with markers, colors, and line style
#   3. Label axes and add grid lines
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

average_price = df.groupby('Category')['Price'].mean()

df['Sales'] = df['Quantity'] * df['Price']
plt.plot(average_price.index,average_price.values,marker ='o',color = 'Orange',linestyle = '-')

plt.title('Category-wise Average Price')
plt.xlabel('Category')
plt.ylabel('Price')
plt.grid()
plt.show()