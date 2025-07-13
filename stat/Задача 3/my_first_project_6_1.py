# H_0: Немає залежності між категоріями даних
# H_1: Категорії з даними маєють залежність

import pandas as pd
from scipy.stats import chi2_contingency, chi2

# Зчитування Excel файлу
file_path = r"C:\Users\User\Desktop\TTT.xlsx"
df = pd.read_excel(file_path)

# Приведення значень до типу bool
df['Add'] = df['Add'].astype(bool)

# Групування по 'Group' і підрахунок TRUE/FALSE
result = df.groupby('Group')['Add'].value_counts().unstack(fill_value=0)
print(result)
# Перейменування колонок (опціонально)
result.columns = ['FALSE', 'TRUE'] if False in result.columns else result.columns

# Перетворення до NumPy масиву
observed = result[['FALSE', 'TRUE']].values

# Застосування тесту Хі-квадрат (Перевірка на залежність)
alpha = 0.05
chi2_stat, p_value, dof, expected  = chi2_contingency(observed)
critical_value = chi2.ppf(1-alpha, dof)
print(f"Критичне значення x^2 = {critical_value}")
print(f"x^2 = {chi2_stat}")
print(f"Ступені свободи: {dof}")
print(f"p-value = {p_value}")


if p_value < alpha:
    print("Відхиляємо нульову гіпотезу — існує залежність між групою та заняттями на канікулах.")
else:
    print("Приймаємо нульову гіпотезу — зв'язку між групою та заняттями на канікулах немає.")
