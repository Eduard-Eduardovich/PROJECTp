
try:
    with open('people.txt', 'r', encoding='utf-8') as file_info:
        count_line = 0
        count_symbols = 0
        for line in file_info:
            count_line += 1
            line = line.strip()
            line_length = len(line)

            if line_length < 3:
                   raise BaseException(f'Ошибка: менее трёх символов в строке {count_line}.')
            else:
                count_symbols += line_length

    print('Ответ в консоли:')
    print(f'Общее количество символов без пробелов и символа новой строки: {count_symbols}')
finally:
    print('Общее количество символов:', count_symbols)




        
