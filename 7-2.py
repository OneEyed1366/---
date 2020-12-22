from abc import ABC, abstractmethod

class Clothes(ABC):
	def suit(self):
		pass

	def coat(self):
		pass

class Suit(Clothes):
	h = 1.86
	@property
	def suit(self):
		return f'Для костюма потребуется, примерно, {round(self.h * 2 + 0.3, 2)} метров ткани'

class Coat(Clothes):
	v = 52
	@property
	def coat(self):
		return f'Для пальто потребуется, примерно, {round(self.v / 6.5 + 0.5, 2)} метров ткани'
	

print(Suit().suit)
print(Coat().coat)
