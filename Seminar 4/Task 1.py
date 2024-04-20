# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

from random import randint

# var2 = set(randint(1, 20) for i in range(int(var1[0])))
# print(var2)

# var3 = set(randint(1, 20) for i in range(int(var1[2])))
# print(var3)

var2_list = [int(i) for i in var2.split()]
print(var2_list)

var3_list = [int(i) for i in var3.split()]
print(var3_list)

var2_set = {*var2_list}
print(str(type(var2_set)))
print(var2_set)


var3_set = {*var3_list}
print(str(type(var3_set)))
print(var3_set)

var4 = sorted(var2_set.intersection(var3_set))
print(*var4)