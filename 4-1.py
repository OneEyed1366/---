from sys import argv

script_name, time_on_work, paid_per_hour, premial = argv

print(
	'Название скрипта: {0}\nВремя на работе: {1}\nОплата в час: {2}\nПремия: {3}\n\nНужно выплатить сотруднику: {4}'.format(
		script_name, time_on_work, paid_per_hour, premial, (int(time_on_work) * int(paid_per_hour)) + int(premial)))