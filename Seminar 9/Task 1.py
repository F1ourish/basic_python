import pandas as pd

df = pd.read_csv('california_housing_train.csv')
filtered_df = df[(df['population'] > 0) & (df['population'] <= 500)]
avg = filtered_df['median_house_value'].mean()
print(f'Средняя стоимость дома с населением от 0 до 500: {avg}')