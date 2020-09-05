from itertools import cycle, count

def integer_generator(begin):
	for num in count(begin):
		if num == 101:
			break
		else:
			print('Повтор №{0}'.format(num))

def repeat_smth_from_list(*args):
	i = 0

	for smth in cycle(args):
		i += 1

		if i == 101:
			break
		else:
			print('Повтор №{0}, содержимое повтора: {1}'.format(i, smth))

integer_generator(2)
repeat_smth_from_list(1, 2, 'text')