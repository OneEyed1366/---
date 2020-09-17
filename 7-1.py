matrix_list_1 = [
	[31, 22],
	[37, 43],
	[51, 86]
]
matrix_list_2 = [
	[11, 32],
	[47, 72],
	[53, 81]
]

class Matrix:
	def __init__(self, list):
		self.list = list

	def __str__(self):
		return '\n'.join(
			' '.join(map(str, row)) for row in self.list)

	def __add__(self, other):
		result = [
		[self.list[row][place] + other.list[row][place], self.list[row][place + 1] + other.list[row][place + 1]
		] for row in range(len(self.list)) for place in range(len(self.list[row]) - 1)]

		return '\n'.join(
			' '.join(map(str, row)) for row in result)

		
m_1 = Matrix(matrix_list_1)
m_2 = Matrix(matrix_list_2)
print(f'Вывод матрицы:\n{m_2}')
print(f'Сложение 2 матриц:\n{m_1 + m_2}')