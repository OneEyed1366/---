def check(number):
	while number == 0:
		number = int(
			input(
				'Введите число больше 0!'
				)
			)

	return number


print(
    round(
        check(int(input('Введите 1 число!'))) / check(int(input('Введите 2 число!'))), 
        1))
