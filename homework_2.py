text = 'Добрый день! Выберите функцию для запуска!\n\n1: Проверка типов данных с выводом результата на экран\n2: Ввод и обмен значений внутри списка\n3: Определение времени года по введённому числу\n4: Вывод введённых слов построчно, с органичением по длине слова\n5: Изменение рейтинга пользователем\n6: Добавление товаров в каталог, с итоговым перечислением характеристик всех товаров\n'

# Функция проверка корректности числа
def check(number, less, more):
    while number < less or number > more:
        number = int(input('Введите корректное число!\n'))
    
    return number
# Функция определения типов данных    
def types_in_list():
    list = [
        'word',
        True,
        1,
        (),
        [],
        {}
        ]
    
    for l in list:
        text = 'Тип объекта: {0}'.format(type(l))
        
        print(text)
# Функция ввода и обмена значений внутри списка        
def input_list():
    array = []
    num = 0
    
    for i in range(int(input('Добрый день!\nКакое количество чисел добавить в список?\n'))):
        array.append(input('Добавьте {} значение: '.format(i + 1)))
        
    for i in range(len(array) // 2):
        array[num], array[num + 1] = array[num + 1], array[num]
        
        num += 2
    
    text = 'Итак, в нынешнем списке {0} элементов\n\nСодержимое списка: {1}'.format(len(array), array)
    
    print(text)
# Функция ввода и определения месяца в промежутке от 1 до 12        
def input_month():
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumm = [9, 10, 11]
    seasons = {
        'Зима': winter,
        'Весна': spring,
        'Лето': summer,
        'Осень': autumm
    }
    
    month = check(
        int(
            input('Добрый день!\nВведите целое число от 1 до 12!\n')
            ), 
            1, 
            12
            )
    
    for season in seasons:
        if month in seasons[season]:
            print('Вы ввели {0} месяц, это {1}!'.format(month, season))
# Функция ввода/вывода слов построчно, с ограничием по длине выводимого слова
def input_words():
    words = input('Добрый день!\nВведите несколько слов, разделив их пробелами!\nВы ввели: ')
    num = 1
    
    for word in words.split():
        print('{0} строка: {1}'.format(num, word[ : 10]))
        
        num += 1
# Функция построения динамичного рейтинга, с учётом исторических данных        
def dynamic_rating():
    raw_rating = [7, 5, 3, 2]
    inp = 1
        
    while inp != 0:
        inp = check(
            int(
                input('Введите любое число от 1 до 10!\n\nЧтобы остановить игру, введите "0"\n'),
                ),
                0,
                10
                )
                
        if inp != 0:
            for rating in raw_rating:
                if inp > max(raw_rating):
                    raw_rating.insert(0, inp)
                elif inp <= min(raw_rating):
                    raw_rating.append(inp)
                elif inp in raw_rating:
                    raw_rating.insert(raw_rating.index(inp) + 1, inp)
                else:
# Схитрил. Не придумал, как должно работать последнее условие, поэтому - сделал сортировку с помощью функции. 
                    raw_rating.append(inp)
                    raw_rating.sort(reverse = True)
                    
                break
                
            print('Список обновился!\nТеперь он имеет следующий вид: {}'.format(raw_rating))
            
        else:
            print('Ясно! Завершаю игру...\n\nХорошего дня!')
# Функция добавления товаров, с выводом аналатики по каждой характеристики товара
def shop():
    result = {}
    shop_list = []
    inp = ''
    num = 1
    names = [
        'Название',
        'Цена',
        'Количество',
        'Единица измерения'
        ]
        
    while inp != '0':
        dict = {}
        
        print('Добавляем {0} товар!'.format(num))
        
        for name in names:
            inp = input('Введите параметр: {0}\n\nЧтобы прекратить добавление товаров, введите "0"'.format(name))
                
            if inp != '0':
                dict.update({name: inp})
            else:
                print('Ясно! Завершаю добавление товаров.\n\nХорошего дня!')
                
                break
        
        if inp != '0':
            shop_list.append((num, dict))
        
            num += 1
    
    for name in names:
        content = []
        
        for product in shop_list:
            content.append(product[1][name])
            
        result.update({name: content})
    
    print('Также, отправляю Вам аналитику о предоставленных товарах!\n\n{0}'.format(result))
            
dict_of_functions = {
    '1': 'types_in_list()',
    '2': 'input_list()',
    '3': 'input_month()',
    '4': 'input_words()',
    '5': 'dynamic_rating()',
    '6': 'shop()'
}


eval(
    dict_of_functions.get(
        input(text)
        )
    )
    
