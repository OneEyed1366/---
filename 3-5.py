i = 0
number = 1
numbers = []

while number != '0':
    i += 1
    
    if i == 1:
        text = 'Добрый день!\nВведите несколько чисел через пробел!\n\nЧтобы остановить выполнение программы, введите "0"!'
    else:
        text = '\n\nВведите несколько чисел через пробел!\n\nЧтобы остановить выполнение программы, введите "0"!'
    
    for number in input(text).split():
        numbers.append(int(number))
    
    print('\nРезультат сложения чисел: {0}'.format(sum(numbers)))
    
    if number == '0':
        print('Завершаю выполнение программы!\nХорошего дня!')
