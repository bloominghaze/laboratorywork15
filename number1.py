import pandas as pd

employees = {
    "Іванов": (15000, "чоловік"),
    "Петрова": (12000, "жінка"),
    "Сидоров": (18000, "чоловік"),
    "Кузнєцова": (11000, "жінка"),
    "Мельник": (14000, "чоловік"),
    "Смирнова": (11500, "жінка"),
    "Федоров": (19000, "чоловік"),
    "Левченко": (12500, "жінка"),
    "Сергієнко": (16000, "чоловік"),
    "Гончарова": (13000, "жінка")
}

df = pd.DataFrame.from_dict(employees, orient='index', columns=['Зарплата', 'Стать'])
df.index.name = 'Прізвище'

print("Дані про співробітників:")
print(df)

grouped_by_gender = df.groupby('Стать').agg({'Зарплата': ['mean', 'min', 'max']})

print("\nАгреговані дані за статтю:")
print(grouped_by_gender)
