def my_func(*args):
	result = list(args)

	del result[result.index(min(result))]

	return sum(result)

print(my_func(8, 2, 4))