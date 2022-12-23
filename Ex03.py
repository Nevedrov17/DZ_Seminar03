import random

def random_list(my_list, n):
    for i in range(0, n):
        my_list.append(round(random.uniform(1, 10), 2))
    print(my_list)
    return my_list
my_list = []
n = int(input('Введите количество элементов в списке: '))
random_list(my_list, n)

new_list = []
for i in my_list:
    new_list.append(round(i % 1, 2))
min = new_list[0]
for i in range(0, len(new_list)):
    if new_list[i] < min:
        min = new_list[i]
print('Минимальное значение=', min)
max = new_list[0]
for i in range(0, len(new_list)):
    if new_list[i] > max:
        max = new_list[i]
print('Максимальное значение=', max)
print('Разница между макс и мин =', max-min)