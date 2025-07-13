# H_0: Немає статистично значущої різниці між результатами в першому та другому семестрах в середині групи
# H_1: Присутня статистично значуща різниця між результатами в першому та другому семестрах в середині групи

import pandas as pd
from scipy.stats import ttest_rel
import matplotlib.pyplot as plt

# Зчитування даних
file_path = r"C:\Users\User\Desktop\TTT.xlsx"
df = pd.read_excel(file_path)

# Поділ за семестрами
df_term1 = df[df['Term'] == 1]
df_term2 = df[df['Term'] == 2]

# Поділ на групи
df_termA_1 = df_term1[df_term1["Group"]=='А']
df_termA_2 = df_term2[df_term2["Group"]=='А']
df_termB_1 = df_term1[df_term1["Group"]=='Б']
df_termB_2 = df_term2[df_term2["Group"]=='Б']
df_termC_1 = df_term1[df_term1["Group"]=='В']
df_termC_2 = df_term2[df_term2["Group"]=='В']

# Знаходимо спільних студентів у 1-му та 2-му семестрах в кожній групі
common_ids_A = set(df_termA_1['ID']).intersection(df_termA_2['ID'])
common_ids_B = set(df_termB_1['ID']).intersection(df_termB_2['ID'])
common_ids_C = set(df_termC_1['ID']).intersection(df_termC_2['ID'])

# Фільтрація спільних учнів у групах
df_termA_1_filtered = df_termA_1[df_termA_1['ID'].isin(common_ids_A)]
df_termA_2_filtered = df_termA_2[df_termA_2['ID'].isin(common_ids_A)]
df_termB_1_filtered = df_termB_1[df_termB_1['ID'].isin(common_ids_B)]
df_termB_2_filtered = df_termB_2[df_termB_2['ID'].isin(common_ids_B)]
df_termC_1_filtered = df_termC_1[df_termC_1['ID'].isin(common_ids_C)]
df_termC_2_filtered = df_termC_2[df_termC_2['ID'].isin(common_ids_C)]

# Вибір стовпця Result і перетворення в список
results_A_1 = df_termA_1_filtered['Result'].tolist()
results_A_2 = df_termA_2_filtered['Result'].tolist()
results_B_1 = df_termB_1_filtered['Result'].tolist()
results_B_2 = df_termB_2_filtered['Result'].tolist()
results_C_1 = df_termC_1_filtered['Result'].tolist()
results_C_2 = df_termC_2_filtered['Result'].tolist()

# Задаємо значення альфа
alpha = 0.05

# Застосування t-тесту
t_stat_A, p_value_A = ttest_rel(results_A_1, results_A_2)
print(f"Група А: t-статистика = {t_stat_A:.3f}, p-value = {p_value_A:.4f}")

# Робимо висновок з отриманих значень
if p_value_A < alpha:
    print("Відхиляємо нульову гіпотезу: є статистично значуща різниця між середніми значеннями групи А, в першому та другому семестрах.")
else:
    print("Приймаємо нульову гіпотезу: статистично значущої різниці між групою А, в першому та другому семестрах не виявлено.")

t_stat_B, p_value_B = ttest_rel(results_B_1, results_B_2)
print(f"Група Б: t-статистика = {t_stat_B:.3f}, p-value = {p_value_B:.4f}")

# Робимо висновок з отриманих значень
if p_value_B < alpha:
    print("Відхиляємо нульову гіпотезу: є статистично значуща різниця між середніми значеннями групи Б, в першому та другому семестрах.")
else:
    print("Приймаємо нульову гіпотезу: статистично значущої різниці між групою Б, в першому та другому семестрах не виявлено.")

t_stat_C, p_value_C = ttest_rel(results_C_1, results_C_2)
print(f"Група С: t-статистика = {t_stat_C:.3f}, p-value = {p_value_C:.4f}")

# Робимо висновок з отриманих значень
if p_value_C < alpha:
    print("Відхиляємо нульову гіпотезу: є статистично значуща різниця між середніми значеннями групи С, в першому та другому семестрах.")
else:
    print("Приймаємо нульову гіпотезу: статистично значущої різниці між групою С, в першому та другому семестрах не виявлено.")


# Побудова boxplot-ів
data = [
    results_A_1, results_A_2,
    results_B_1, results_B_2,
    results_C_1, results_C_2
]

labels = [
    'A Семестр 1', 'A Семестр 2',
    'Б Семестр 1', 'Б Семестр 2',
    'В Семестр 1', 'В Семестр 2'
]

colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightgray', 'lightpink']

fig, ax = plt.subplots(figsize=(10,6))
box = ax.boxplot(data, patch_artist=True, labels=labels)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Порівняння результатів по семестрах і групах')
ax.set_ylabel('Оцінки')

plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()