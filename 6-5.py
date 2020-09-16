class Stationery:
	def __init__(self, title):
		self.title = title

	def draw(self):
		print('Запуск отрисовки, иструмент: {0}'.format(self.title))

class Pencil(Stationery):
	def __init__(self):
		super().__init__(title = 'Карандаш')

class Pen(Stationery):
	def __init__(self):
		super().__init__(title = 'Ручка')

class Handle(Stationery):
	def __init__(self):
		super().__init__(title = 'Маркер')

Pencil().draw() 
Pen().draw()
Handle().draw()