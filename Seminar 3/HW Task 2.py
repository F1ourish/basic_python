# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

from math import fabs

list_1 = [1, 12, 6, 7, 8, 15]
k = 11

temp = k - list_1[0]

for i in range(len(list_1)):
    if temp >= abs(k - list_1[i]):
        temp = abs(k - list_1[i])
        j = i
        
print(list_1[j])