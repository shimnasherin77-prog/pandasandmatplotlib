# Sample Dataset ⿢: Age vs Annual Income by Gender
import matplotlib.pyplot as plt
import pandas as pd
df_income = pd.DataFrame({
    'Age': [22, 25, 27, 29, 30, 32, 35, 37, 40, 45],
    'Annual Income': [25000, 27000, 30000, 33000, 36000, 40000, 45000, 48000, 52000, 60000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})

# ⿢ Plot a scatter graph comparing 'Age' and 'Annual Income' from the dataset.
#     - Use different colors or markers for different 'Gender' categories.
plt.scatter(df_income[df_income['Gender'] == 'Male']['Age'],
            df_income[df_income['Gender'] == 'Male']['Annual Income'], marker='o', s=80, label='Male')

plt.scatter(df_income[df_income['Gender'] == 'Female']['Age'],
            df_income[df_income['Gender'] == 'Female']['Annual Income'], marker='^', s=80, label='Female')

plt.xlabel("Age")
plt.ylabel("Annual Income")
plt.title("Age vs Annual Income by Gender")
plt.show()