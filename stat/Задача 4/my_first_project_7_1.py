# H_0: Немає різниці між оцінками учнів, що ходили влітку на заняття і тими, що не відвідували їх
# H_1: Статистично значуща різниця між групами присутня

from scipy.stats import ttest_ind
import pandas as pd
import matplotlib.pyplot as plt

# Зчитування даних
file_path = r"C:\Users\User\Desktop\TTT.xlsx"
df = pd.read_excel(file_path)

# Перетворення значень у колонці Add до логічного типу
df['Add'] = df['Add'].astype(bool)

# Поділ на дві групи
group_true_df = df[df['Add'] == True]
group_false_df = df[df['Add'] == False]

# Витягування стовпця 'Result'
group_true = group_true_df['Result']
group_false = group_false_df['Result']

# t-тест для незалежних вибірок з припущенням рівності дисперсій
t_stat, p_value = ttest_ind(group_true, group_false, equal_var=True)

# Виведення результатів
print("t-статистика:", t_stat)
print("p-значення:", p_value)

# Інтерпретація
alpha = 0.05
if p_value < alpha:
    print("Відхиляємо нульову гіпотезу: є статистично значуща різниця між середніми значеннями двох груп.")
else:
    print("Приймаємо нульову гіпотезу: статистично значущої різниці між групами не виявлено.")

# Побудова боксплотів
data = [group_true, group_false]

plt.figure(figsize=(7,5))
box = plt.boxplot(data, labels=['Відвідували', 'Не відвідували'], patch_artist=True)

colors = ['#4c72b0', '#dd8452']

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.title('Порівняння результатів за групами, що ходили на заняття влітку', fontsize=14, fontweight='bold')
plt.ylabel('Result')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
