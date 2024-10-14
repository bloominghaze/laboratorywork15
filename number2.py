import pandas as pd
import matplotlib.pyplot as plt

file_path = 'comptagevelo20152.csv'
df = pd.read_csv(file_path, sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

print("Перші рядки даних:")
print(df.head())

df_2015 = df[df.index.year == 2015]

print("\nДані за 2015 рік:")
print(df_2015.head())

df_2015 = df_2015.apply(pd.to_numeric, errors='coerce')

df_2015['Month'] = df_2015.index.month

monthly_totals = df_2015.groupby('Month').sum()

print("\nАгреговані дані по місяцях за 2015 рік:")
print(monthly_totals)

most_popular_month = monthly_totals.sum(axis=1).idxmax()
print(f'\nНайпопулярніший місяць: {most_popular_month}')

monthly_totals.plot(kind='bar', figsize=(10, 6))
plt.title('Використання велодоріжок по місяцях у 2015 році')
plt.xlabel('Місяць')
plt.ylabel('Кількість поїздок')
plt.show()
