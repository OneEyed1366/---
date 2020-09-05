def fact(n):
	result = 1

	for num in range(1, n):
		result *= num

		yield result

for i in fact(4):
	print(i)