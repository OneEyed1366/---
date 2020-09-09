def int_func(*args):
    for arg in args:
        print('Начальное слово: {0}, итоговое слово: {1}'.format(arg, arg.capitalize()))

for text in input('Добрый день!\nВведите несколько слов с маленькой буквы!').split():
    int_func(text)
