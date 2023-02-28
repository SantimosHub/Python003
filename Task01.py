# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

list_lenght = int(input('Введите длину списка: '))
number = int(input('Введите число от 0 до 100: '))
list = [random.randint(1, 100) for _ in range(list_lenght)]
print (list)
count = 0
max_nearly = 100
for i in range(0, list_lenght):
     if list[i] == number: count +=1
     if abs(list[i]-number)<max_nearly: max_nearly= list[i]

print(f"Число встречается {count} раз" if count>0 else f"Максимально близкое число {max_nearly}" )
