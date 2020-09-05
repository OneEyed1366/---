from functools import reduce

result = [num for num in range(100, 1001) if num % 2 == 0]

def list_generation(prev_el, el):

	return prev_el + el

print(reduce(list_generation, result))