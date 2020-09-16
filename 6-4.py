class Car:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print('{0} полетела! Точнее, пока поехала...'.format(self.name))

	def stop(self):
		print('{0} остановилась для отдыха! Отдыхаем...'.format(self.name))

	def turn(self, direction):
		print('{0} повернула {1}!'.format(self.name, direction))

	def show_speed(self, max):
		if self.is_police == True:
			print('Вау! Мы на полецейской машине, зовут {0}!\nПреследуем преступника на скорости {1} км/ч!'.format(
				self.name,
				self.speed))
		elif self.speed > max:
			print('Уже не смешно, {0}! Тормози!!'.format(self.name))
		else:
			print('Текущая скорость: {0} км/ч'.format(self.speed))

class TownCar(Car):
	def __init__(self):
		super().__init__(speed = 65, color = 'Коричневый', name = 'Грязевик', is_police = False)

class WorkCar(Car):
	def __init__(self):
		super().__init__(speed = 55, color = 'Зелёный', name = 'Лошадка', is_police = False)

class SportCar(Car):
	def __init__(self):
		super().__init__(speed = 120, color = 'Красный', name = 'Дама в красном', is_police = False) 

class PoliceCar(Car):
	def __init__(self):
		super().__init__(speed = 4000, color = 'Синий с чёрным', name = 'Догонялка', is_police = True)

TownCar().show_speed(60)
WorkCar().show_speed(40)
SportCar().go()
SportCar().turn('Налево')
SportCar().stop()
PoliceCar().show_speed(30)
