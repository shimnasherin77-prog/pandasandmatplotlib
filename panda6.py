import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

df['Sales'] = df['Quantity'] * df['Price']

total_sales = df.groupby('Country')['Sales'].sum()

# Set figure size for better visibility
plt.figure(figsize=(10, 8))  # width=10, height=8 inches

plt.pie(
    total_sales.values,
    labels=total_sales.index,
    autopct='%1.1f%%',
    shadow=True,
)
plt.axis('equal')
plt.title("Sales by Country", fontsize=14)
plt.tight_layout()  # adjust layout
plt.show()

