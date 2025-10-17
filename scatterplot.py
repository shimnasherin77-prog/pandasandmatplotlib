import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 📊 SCATTER PLOT QUESTIONS
# ============================================================

# Sample Dataset ⿡: Study hours vs Score

df_study = pd.DataFrame({
    'Hours Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [35, 40, 50, 55, 65, 70, 75, 80, 88, 95]
})
# ⿡ Create a scatter plot showing the relationship between 'Hours Studied' and 'Score' from the dataset.
#     - Label the X-axis as "Hours Studied" and Y-axis as "Score".
#     - Add a title: "Study Hours vs Student Score".

plt.title('Study Hours vs Student Score')
plt.xlabel('Hours studied ')
plt.ylabel('Score')
plt.scatter(df_study['Hours Studied'],df_study['Score'],color = 'Blue',
            s = 50,
            label = 'Score')
plt.show()