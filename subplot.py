# ============================================================
# 🧩 SUBPLOTS QUESTIONS
# ============================================================
import matplotlib.pyplot as plt
import pandas as pd
# Sample Dataset ⿥: Category and Quantity
df_sales = pd.DataFrame({
    'Product Category': ['Electronics', 'Clothing', 'Groceries', 'Toys', 'Books'],
    'Quantity Sold': [120, 200, 150, 90, 130]
})

# ⿥ Create a subplot with two plots side by side:
#     - Left plot: Bar chart of 'Product Category' vs 'Quantity Sold'.
#     - Right plot: Pie chart showing 'Category' wise sales percentage.

figure,axes = plt.subplots(1,2)
axes[0].bar(df_sales['Product Category'], df_sales['Quantity Sold'], color='skyblue')
axes[1].pie(
    df_sales['Quantity Sold'],labels=df_sales['Product Category'],autopct='%1.1f%%',)
plt.show()