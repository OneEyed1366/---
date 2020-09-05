def from_to():
	result = [num for num in range(20, 240) if num % 20 == 0 or num % 21 == 0]

	print(result)

from_to()