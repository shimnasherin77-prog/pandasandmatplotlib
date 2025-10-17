import matplotlib.pyplot as plt
import pandas as pd
# Sample Dataset ⿣: Customer Age Distribution
df_age = pd.DataFrame({
    'Customer Age': [18, 20, 22, 22, 25, 26, 27, 29, 30, 32, 34, 35, 36, 38, 40, 42, 45, 48, 50, 52]
})

# ⿣ Plot a histogram of the 'Customer Age' column to show the distribution of ages.
#     - Set the number of bins to 10.
#     - Add proper labels and a title.
plt.hist(df_age['Customer Age'], bins=10, edgecolor='black', color='skyblue')
plt.title('Customer age')
plt.xlabel('Number of customers')
plt.ylabel('Distribution of customer age')
plt.show()