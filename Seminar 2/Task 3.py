# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример


# n=16

# #Вывод
# 1
# 2
# 4
# 8
# 16


n = 1024
k = 0
while 2**k <= n:
    print(2**k)
    k += 1