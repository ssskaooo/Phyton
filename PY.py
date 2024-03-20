# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
#Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() 


#__________________________________________________________________________________________________________

import pandas as pd
import random

# Создаем исходный DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем столбец 'whoAmI' в one-hot формат с использованием get_dummies
one_hot_data = pd.get_dummies(data['whoAmI'])

# Присоединяем one-hot столбцы к исходному DataFrame
result_data = pd.concat([data, one_hot_data], axis=1)

# Удаляем исходный столбец 'whoAmI'
result_data = result_data.drop('whoAmI', axis=1)

# Выводим результат
print(result_data.head())