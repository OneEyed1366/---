class Length:
	def value():
		return 20

class Width:
	def value():
		return 5000

class Road(Length, Width):
	_length = Length.value()
	_width = Width.value()

	def __init__(self):
		print('{:,} т.'.format(self._length * self._width * 25 * 5 // 1000).replace(',', ' '))

Road()
