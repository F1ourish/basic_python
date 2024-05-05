# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd
import random

# Создание DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Перевод в one hot вид
data['robot'] = data['whoAmI'].apply(lambda x: True if x == 'robot' else False)
data['human'] = data['whoAmI'].apply(lambda x: True if x == 'human' else False)

# Удаление исходного столбца
data = data.drop('whoAmI', axis=1)

print(data.head())