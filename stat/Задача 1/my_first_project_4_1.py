# H_0: Немає статистично значущої різниці між результатами в першому та другому семестрах
# H_1: Присутня статистично значуща різниця між результатами в першому та другому семестрах

import pandas as pd
import numpy as np
from scipy.stats import ttest_rel
import matplotlib.pyplot as plt

# Зчитування даних
file_path = r"C:\Users\User\Desktop\TTT.xlsx"
df = pd.read_excel(file_path)

# Поділ за семестрами
df_term1 = df[df['Term'] == 1]
df_term2 = df[df['Term'] == 2]

# Знаходимо спільні ID учнів, які були в обох семестрах
common_ids = set(df_term1['ID']).intersection(df_term2['ID'])

# Фільтруємо, залишаючи лише спільних учнів
df_term1_common = df_term1[df_term1['ID'].isin(common_ids)]
df_term2_common = df_term2[df_term2['ID'].isin(common_ids)]

# Відсортуємо за ID
df_term1_common_sorted = df_term1_common.sort_values('ID')
df_term2_common_sorted = df_term2_common.sort_values('ID')

# Візьмемо по одному запису на кожного учня (перший за ID)
df_term1_unique = df_term1_common_sorted.drop_duplicates(subset='ID', keep='first')
df_term2_unique = df_term2_common_sorted.drop_duplicates(subset='ID', keep='first')

# Формуємо списки результатів
results_term1 = df_term1_unique['Result'].tolist()
results_term2 = df_term2_unique['Result'].tolist()

# Функція для обчислення статистик
def describe_stats(data):
    data_np = np.array(data)
    mean = np.mean(data_np)
    var = np.var(data_np, ddof=1)  # несмещена дисперсія
    std = np.std(data_np, ddof=1)  # стандартне відхилення
    quantiles = np.quantile(data_np, [0.25, 0.5, 0.75])
    return mean, var, std, quantiles

mean1, var1, std1, quantiles1 = describe_stats(results_term1)
mean2, var2, std2, quantiles2 = describe_stats(results_term2)

print("Статистики для 1-го семестру:")
print(f"Математичне сподівання (середнє оцінок): {mean1}")
print(f"Дисперсія: {var1}")
print(f"Стандартне відхилення: {std1}")
print(f"Квантілі (25%, 50%, 75%): {quantiles1}")

print("Статистики для 2-го семестру:")
print(f"Математичне сподівання (середнє оцінок): {mean2}")
print(f"Дисперсія: {var2}")
print(f"Стандартне відхилення: {std2}")
print(f"Квантілі (25%, 50%, 75%): {quantiles2}")

# Парний t-тест (приймаємо нульову гіпотезу, про те що різниці в їх результатах немає)
t_stat, p_value = ttest_rel(results_term1, results_term2)
print(f"Парний t-тест: t-статистика = {t_stat:.3f}, p-value = {p_value:.4f}")

# Задаємо значення альфа
alpha = 0.05

# Робимо висновок з отриманих значень
if p_value < alpha:
    print("Відхиляємо нульову гіпотезу: є статистично значуща різниця між середніми значеннями двох груп.")
else:
    print("Приймаємо нульову гіпотезу: статистично значущої різниці між групами не виявлено.")

# Будуємо boxplot-и
colors = ['lightblue', 'lightgreen']

plt.figure(figsize=(8,6))
box = plt.boxplot([results_term1, results_term2], labels=['С1', 'С2'], patch_artist=True)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.2)

plt.setp(box['whiskers'], color='black', linewidth=1.2)
plt.setp(box['caps'], color='black', linewidth=1.2)
plt.setp(box['medians'], color='red', linewidth=2)

plt.title('Порівняння оцінок за семестрами')
plt.ylabel('Оцінки (Result)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
