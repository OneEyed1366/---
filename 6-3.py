wage = 2000
bonus = 500

class Worker:
	name = 'Андрей'
	surname = 'Прокопенко'
	position = 'Стажёр'
	_income = {
	'wage': wage,
	'bonus': bonus
	}

class Position(Worker):
	def get_full_name(self):
		print('ФИО: {0} {1}'.format(self.name, self.surname))

	def get_total_income(self):
		print('Итоговый доход: {2}\n\nОклад: {0}\nПремия: {1}'.format(
			self._income['wage'],
			self._income['bonus'],
			self._income['wage'] + self._income['bonus'])
		)

Position().get_full_name()
Position().get_total_income()