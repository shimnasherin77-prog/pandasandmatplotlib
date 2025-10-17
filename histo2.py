import matplotlib.pyplot as plt
import pandas as pd
# Sample Dataset ⿤: Purchase Amounts
df_purchase = pd.DataFrame({
    'Purchase Amount': [120, 250, 300, 150, 500, 600, 800, 400, 350, 700, 900, 1000, 150, 200, 650]
})

# ⿤ Draw a histogram to display the frequency of 'Purchase Amount' in the dataset.
#     - Use edgecolor='black' for better visibility of bins.
#     - Add gridlines to make it more readable.
plt.hist(df_purchase['Purchase Amount'], bins=10, edgecolor='black', color='skyblue')
plt.title('Purchase Amount')
plt.grid()
plt.show()
