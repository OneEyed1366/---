import sys, time

class TrafficLight():
	__color = []

	def check(self):
		if (self.__color[0] != 'Красный') or (
			self.__color[1] != 'Жёлтый') or (
			self.__color[2] != 'Зелёный'):
			print('Ошибка!\nЗавершаю выполнение программы!')

			sys.exit()

	def running(self, *args):
		for arg in args:
			self.__color.append(arg)

		time.sleep(5)
		print(self.__color[0])

		time.sleep(2)
		print(self.__color[1])

		time.sleep(15)
		print(self.__color[2])


TrafficLight().running('Красный', 'Жёлтый', 'Зелёный')
TrafficLight().check()
