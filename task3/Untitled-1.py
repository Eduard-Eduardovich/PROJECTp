import random
result_sum = 0
count_probability = 0

while result_sum < 777:
    number = input('Введите число: ')

    result_sum += int(number)
    count_probability += 1

    if random.randint(1, 13) == 1:
        print('Вас постигла неудача!')
        break

    with open('result.txt', 'a') as f:
        f.write(number + '\n')

if result_sum >= 777:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')

print('Содержимое файла result.txt:')
with open('result.txt', 'r') as f:
    for line in f:
        print(line)


