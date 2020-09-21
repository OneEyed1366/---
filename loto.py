import sys, random


class Card():
	def __init__(self, name):
		self.name = name

		raw = sorted(list({random.randrange(1, 90, 1) for num in range(5) for num in range(4)})[ : 15])
		result = [raw[num : : 3] for num in range(3)]
		for i in range(len(result)):
			for n in range(4):
				result[i].insert(random.randrange(1, 9, 1), '')

		self.card = result

	def __str__(self):
		return f'{"-"*3}{self.name}{"-"*3}\n' + '\n'.join(
			' '.join(
				map(str, self.card[num])) for num in range(len(self.card))
			) + f'\n{"-"*18}'

	def __iter__(self):
		self.a = -1

		return self

	def __next__(self):
		if self.a < len(self.card) - 1:
			self.a += 1

			return self.card[self.a]
		else:
			raise StopIteration

	def __getitem__(self, key):
		return self.card[key]
	# @staticmethod
	def check_input(self):
		answer = input('Зачеркнуть цифру? (y/n)')

		while answer != 'y' and answer != 'n':
			answer = input('Вы ввели некорректный ответ!\nПожалуйста, введите "y" или "n"!')

		else:
			return answer
	
	def check_card(self, num, card, answer):
		for i in card:
			if ((i.count(num) > 0) and (answer == 'y')) or (
				(i.count(num) == 0) and (answer == 'n')):
				return True

class Player_1(Card):
	def __init__(self):
		super().__init__('Ваша карточка')


class Player_2(Card):
	def __init__(self):
		super().__init__('Карточка ПК')

barrels = [num for num in range(91)]
random.shuffle(barrels)
barrels_left = 90
gamer_1 = Player_1()
gamer_2 = Player_2()

for barrel in barrels:
	barrels_left -= 1

	print(f'Новый бочонок: {barrel} (осталось {barrels_left})\n{gamer_1}\n{gamer_2}')
	answer = gamer_1.check_input()

	if gamer_1.check_card(barrel, gamer_1, answer):
		for card in gamer_1:
			if card.count(barrel) > 0:
				card[card.index(barrel)] = '-'
	else:
		print(f'Упс!\nУдачи в следующий раз!')
		sys.exit()

	for card in gamer_2:
		if card.count(barrel) > 0:
			card[card.index(barrel)] = '-'
