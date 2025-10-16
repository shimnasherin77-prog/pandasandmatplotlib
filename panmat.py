import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

category_quantity = df.groupby('Category')['Quantity'].sum()
print(category_quantity)          
#line chart
#plt.plot(category_quantity.index,category_quantity.values)
#bar chart
#plt.bar(category_quantity.index,category_quantity.values)
#pie chart
plt.pie(category_quantity.values,
        labels=category_quantity.index,
        shadow=True,
        explode=[0,0,0],
        autopct="%1.1f%%")

plt.title('total quantity sold by category')
plt.xlabel('Category')
plt.ylabel('Total Quantity')

plt.show()
