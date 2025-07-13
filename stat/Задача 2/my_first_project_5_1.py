# H_0: Різниці між результатами оцінок між групами немає
# H_1: Є статистично значущі між результатами оцінок груп

import pandas as pd
from scipy.stats import f_oneway
import matplotlib.pyplot as plt

# Зчитування даних
file_path = r"C:\Users\User\Desktop\TTT.xlsx"
df = pd.read_excel(file_path)

# Відфільтровуємо групи
df_A = df[df['Group'] == 'А']
df_B = df[df['Group'] == 'Б']
df_C = df[df['Group'] == 'В']

# Вибираємо результати
results_A = df_A['Result'].tolist()
results_B = df_B['Result'].tolist()
results_C = df_C['Result'].tolist()

# Проводимо однофакторний ANOVA тест
f_stat, p_value = f_oneway(results_A, results_B, results_C)

print(f"ANOVA F-статистика: {f_stat:.3f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Відхиляємо нульову гіпотезу: принаймні одна група відрізняється статистично значущо")
else:
    print("Немає підстав відхиляти нульову гіпотезу: групи не мають статистично значущих відмінностей")

# Для візуалізації будуємо boxplot
data = [results_A, results_B, results_C]
labels = ['Група А', 'Група Б', 'Група В']
colors = ['#89CFF0', '#90EE90', '#FF7F7F']
fig, ax = plt.subplots(figsize=(8,6))
box = ax.boxplot(data, patch_artist=True, labels=labels)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for whisker in box['whiskers']:
    whisker.set(color='black', linewidth=1.5)
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
for median in box['medians']:
    median.set(color='darkred', linewidth=2)

ax.set_title('Порівняння результатів трьох груп (ANOVA)', fontsize=14)
ax.set_ylabel('Оцінки', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
