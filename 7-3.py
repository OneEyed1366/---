class Cell:
	def __init__(self, amount):
		self.amount = amount

	def __add__(self, other):
		return self.amount + other.amount

	def __sub__(self, other):
		if self.amount - other.amount > 0:
			return self.amount - other.amount
		else:
			return 'Ошибка! Клеток меньше 0!!'

	def __mul__(self, other):
		return self.amount * other.amount

	def __truediv__(self, other):
		return self.amount // other.amount

	def make_order(self, cells):
		return '\\n'.join(
			f'{"*" * cells}' for cell in range(self.amount // cells)) + f'\\n{"*" * (self.amount % cells)}'
	

c_1 = Cell(13)
c_2 = Cell(5)

print(f'Сумма клеток: {c_1 + c_2}')
print(f'Разность клеток: {c_1 - c_2}')
print(f'Перемножение клеток: {c_1 * c_2}')
print(f'Деление клеток(целочисленное): {c_1 / c_2}')
print(f'Упорядочивание клеток: {c_1.make_order(4)}')