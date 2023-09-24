def calculate(line):
    try:
        operand1, symbol, operand2 = line.split()
        operand1 = int(operand1)
        operand2 = int(operand2)
        if symbol == '+':
            return operand1 + operand2
        elif symbol == '-':
            return operand1 - operand2
        elif symbol == '*':
            return operand1 * operand2
        elif symbol == '/':
            return operand1 // operand2
        elif symbol == '%':
            return operand1 % operand2
        else:
            raise ValueError('Неизвестная операция')
    except ValueError as e:
        raise ValueError(f'Ошибка в строке {line}: {e}')



with open('calc.txt') as f:
    lines = f.readlines()
results = []
for line in lines:
    try:
        results.append(calculate(line.strip()))
    except ValueError as e:
        print(f'Обнаружена ошибка в строке: {line}')
        print(e)
        print('Хотите исправить? (Да/Нет)')
        answer = input()
        if answer == 'Да':
            line = input('Введите исправленную строку: ')
            results.append(calculate(line))
print('Сумма результатов:', sum(results))




                    