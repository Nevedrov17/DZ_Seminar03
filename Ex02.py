import random

def random_list(my_list, n):
    for i in range(0, n):
        my_list.append(random.randint(1, 10))
    print(my_list)
    return my_list
my_list = []
n = int(input('Введите количество элементов в списке: '))
random_list(my_list, n)

pr = 0
for i in range(0, len(my_list)//2):
    pr = my_list[i] * my_list[len(my_list) - 1 - i]
    print(pr, end=' ')
if len(my_list) % 2 > 0:
    print(my_list[len(my_list)//2]**2)

