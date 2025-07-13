# H_0: Різниці в результатах оцінок між групами немає
# H_1: Є статистично значущі відмінності між результатами оцінок груп

import pandas as pd
from scipy.stats import f_oneway
import matplotlib.pyplot as plt

# Зчитування даних
file_path = r"C:\Users\User\Desktop\TTT.xlsx"
df = pd.read_excel(file_path)

# Поділ за семестрами
df_term1 = df[df['Term'] == 1]
df_term2 = df[df['Term'] == 2]

# Групи для семестру 1
results_A_1 = df_term1[df_term1['Group'] == 'А']['Result'].tolist()
results_B_1 = df_term1[df_term1['Group'] == 'Б']['Result'].tolist()
results_C_1 = df_term1[df_term1['Group'] == 'В']['Result'].tolist()

# Групи для семестру 2
results_A_2 = df_term2[df_term2['Group'] == 'А']['Result'].tolist()
results_B_2 = df_term2[df_term2['Group'] == 'Б']['Result'].tolist()
results_C_2 = df_term2[df_term2['Group'] == 'В']['Result'].tolist()

# ANOVA для семестру 1
f_stat1, p_value1 = f_oneway(results_A_1, results_B_1, results_C_1)
print("Семестр 1:")
print(f"F-статистика: {f_stat1:.3f}, p-value: {p_value1:.4f}")
if p_value1 < 0.05:
    print("Відхиляємо нульову гіпотезу: є статистично значущі відмінності між групами в першому семесті")
else:
    print("Приймаємо нульову гіпотезу: немає статистично значущих відмінностей між групами в першому семестрі")

# ANOVA для семестру 2
f_stat2, p_value2 = f_oneway(results_A_2, results_B_2, results_C_2)
print("Семестр 2:")
print(f"F-статистика: {f_stat2:.3f}, p-value: {p_value2:.4f}")
if p_value2 < 0.05:
    print("Відхиляємо нульову гіпотезу: є статистично значущі відмінності між групами в другому семесті")
else:
    print("Приймаємо нульову гіпотезу: немає статистично значущих відмінностей між групами в другому семестрі")


# Boxplot для СЕМЕСТРУ 1
data1 = [results_A_1, results_B_1, results_C_1]
labels = ['Група А', 'Група Б', 'Група В']
colors = ['#89CFF0', '#90EE90', '#FF9999']

fig1, ax1 = plt.subplots(figsize=(8, 6))
box1 = ax1.boxplot(data1, patch_artist=True, labels=labels)

for patch, color in zip(box1['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax1.set_title('Boxplot: Групи у Семестрі 1', fontsize=14)
ax1.set_ylabel('Оцінки')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Boxplot для СЕМЕСТРУ 2
data2 = [results_A_2, results_B_2, results_C_2]

fig2, ax2 = plt.subplots(figsize=(8, 6))
box2 = ax2.boxplot(data2, patch_artist=True, labels=labels)

for patch, color in zip(box2['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax2.set_title('Boxplot: Групи у Семестрі 2', fontsize=14)
ax2.set_ylabel('Оцінки')
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()