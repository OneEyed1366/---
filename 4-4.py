from itertools import count

def not_in_list(*args):
	result = [num for num in args if args.count(num) == 1]

	print(result)

not_in_list(0, 1, 1, 1, 2, 87, 3, 4, 4, 5, 67)