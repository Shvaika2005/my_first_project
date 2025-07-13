# H_0: Різниці між учнями що відвідували і невідвідували заняття влітку та додаткові немає
# H_1: Є значна статистична різниця між результатами цих груп

import pandas as pd
from scipy.stats import f_oneway  # ANOVA
import matplotlib.pyplot as plt

# Зчитування даних
file_path = r"C:\Users\User\Desktop\TTT.xlsx"
df = pd.read_excel(file_path)

# Приведення колонок 'Add' і 'Ext' до типу bool
df['Add'] = df['Add'].astype(bool)
df['Ext'] = df['Ext'].astype(bool)

# Фільтрація по групах
group_1 = df[(df['Add'] == True) & (df['Ext'] == True)]
group_2 = df[(df['Add'] == False) & (df['Ext'] == False)]
group_3 = df[(df['Add'] == False) & (df['Ext'] == True)]
group_4 = df[(df['Add'] == True) & (df['Ext'] == False)]

# Зводимо результати учнів до списків
group_1_results = group_1['Result'].tolist()
group_2_results = group_2['Result'].tolist()
group_3_results = group_3['Result'].tolist()
group_4_results = group_4['Result'].tolist()

# Проводимо однофакторний ANOVA тест
f_stat, p_value = f_oneway(group_1_results, group_2_results, group_3_results, group_4_results )
print(f"ANOVA F-статистика: {f_stat:.3f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Відхиляємо нульову гіпотезу: принаймні одна група відрізняється статистично значимо")
else:
    print("Приймаємо нульову гіпотезу: групи не мають статистично значущих відмінностей")


# Побудова боксплотів
data = [group_1_results, group_2_results, group_3_results, group_4_results]
labels = ['Ходили на дод і влітку', 'Не ходили влітку і на дод', 'Не ходили влітку, ходили на дод', 'Ходили влітку, не ходили на дод']
colors = ['#4c72b0', '#dd8452', '#55a868', '#c44e52']

plt.figure(figsize=(10,6))
box = plt.boxplot(data, patch_artist=True, labels=labels)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.title('Порівняння результатів груп за що ходили влітку і на додаткові', fontsize=14, fontweight='bold')
plt.ylabel('Result')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()