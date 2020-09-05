def my_func_1(x, y):

	return x ** y

print(my_func_1(3.1, -5))

def my_func_2(x, y):
	result = x

	for i in range(1, abs(y)):
		result *= x

	if y < 0:
		return 1 / result
	else:
		return result


print(my_func_2(3.1, -5))