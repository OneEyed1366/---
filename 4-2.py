def bigger_number(*args):
	result = [num for num in args if num > args[args.index(num) - 1]]

	print(result)

bigger_number(1, 2, 5, 3, 7, 8, 0)