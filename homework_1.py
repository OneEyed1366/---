text = 'Добрый день! Выберите функцию для запуска!\n\n1: Инициализация переменных и вывод на экран\n2: Форматирование секунд в часы-минуты-секунды\n3: Сумма повторяющегося числа\n4: Нахождение наибольшего числа\n5: Рентабельность организации\n6: Расчёт результатов спортсмена'

# Создание и работа с переменными
def params():
    test1 = 1
    test2 = 'hello, world!'
    test3 = '1 + 1 = {0}'.format(1 + 1)
    test4 = True
    inp_numbers = int(input('Доброго времени суток!\nВведите случайное число!'))
    inp_words = input('А теперь случайное слово...')
    
    for t in [test1, test2, test3, test4, inp_numbers, inp_words]:
        print(t)

# Перевод времени из секунд в формат чч:мм:сс
def time(time_raw):
    mins, secs = divmod(time_raw, 60)
    hours, mins = divmod(mins, 60)
    
    return 'Ясно! Отправляю Вам время в формате "часы:минуты:секунды"\n\n{0} секунд это {1}:{2}:{3}'.format(
        time_raw,
        hours,
        mins, 
        secs
        )

# Сумма чисел числа n
def nums(n, m):
    sums = n
    str_n = str(n)
    sum_str = str(n)
    
    for i in range(1, m):
        sum_str += str_n
        sums += int(sum_str)
        
    return 'Введённое число: {0}\nЧисло повторов: {1}\nРезультат: {2}'.format(
        n,
        m,
        sums
        )
    
# Наибольшее положительное число
def max_num(number):
    start_num = number
    num = -1
    
    while number > 10:
        num_cycle = number % 10
        number //= 10
        
        if num_cycle > num:
            num = num_cycle
    
    return 'Исходное число: {0}\nНаибольше число: {1}'.format(
        start_num,
        num
        )
        
def cash_of_org(revenue, cost):
    revenue_text = 'Поздравляем! Ваша организация вышла в прибыль!'
    cost_text = 'Сожалеем, но - Ваша организация работает в убыток...'
    
    if revenue > cost:
        print(revenue_text)
        
        comrades = int(input('Введите число Ваших сотрудников'))
        
        return 'Ваша общая рентабельность: {0}\nКаждый сотрудник принёс Вам {1}$'.format(
            round((revenue - cost) / revenue, 2),
            round((revenue - cost) / comrades, 3)
            )
    else:
        return cost_text
        
def sport_run(a, b):
    day = 0
    
    while a < b:
        day += 1
        
        if day != 1:
            a += (a * 0.1)
        
        print('{0}-день: {1} км.'.format(
            day,
            round(a, 2)
            ))
            
    return 'На {0}-й день спортсмен достиг результата -- пробежал не менее {1} км.'.format(
        day,
        b
        )
        
dict_of_functions = {
    '1': "params()",
    '2': "print(time(int(input('Добрый день! Введите количество секунд'))))",
    '3': "print(nums(int(input('Добрый день! Введите случайное число!')), 3))",
    '4': "print(max_num(int(input('Добрый день! Введите случайное число, из которого будет выделено наибольшее!'))))",
    '5': "print(cash_of_org(int(input('Введите Вашу прибыль!')), int(input('Введите Ваши издержки!'))))",
    '6': "print(sport_run(int(input('Введите начальный результат спортсмена!')), int(input('Введите дистанцию, которую ему необходимо пробежать!'))))"
}


eval(
    dict_of_functions.get(
        input(text)
        )
    )
