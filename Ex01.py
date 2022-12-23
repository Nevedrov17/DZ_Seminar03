import random

def random_list(my_list, n):
    for i in range(0, n):
        my_list.append(random.randint(1, 10))
    print(my_list)
    return my_list

my_list = []
n = int(input('Введите количество элементов в списке: '))
random_list(my_list, n)

sum = 0
my_index = 0
new_list = []
for i in my_list:
    if my_index %2 != 0:
        sum += i
        new_list.append(i)
    my_index += 1
print('На нечетных позициях элементы', new_list)
print('Сумма элементов на нечетных позициях =', sum)


