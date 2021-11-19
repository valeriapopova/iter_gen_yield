nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]

n_list = [
	['a', 'b', 'c', ['j', ['k', 'l', ['y']]]],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]


def first_generator(some_list):
	for item in some_list:
		for i in item:
			yield i


# example = first_generator(nested_list)
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))


class FirstIterator:
	def __init__(self, some_list):
		self.some_list = some_list

	def __iter__(self):
		self.some_list_iter = iter(self.some_list)
		self.nested_list = []
		self.counter = -1
		return self

	def __next__(self):
		self.counter += 1
		if self.counter == len(self.nested_list):
			self.nested_list = None
			self.counter = 0
			while not self.nested_list:
				self.nested_list = next(self.some_list_iter)
		return self.nested_list[self.counter]


# for item in FirstIterator(nested_list):
# 	print(item)


class SecondIterator():
	def __init__(self, multi_list):
		self.multi_list = multi_list

	def __iter__(self):
		self.iterators_queue = []  # очередь
		self.current_iterator = iter(self.multi_list)
		return self

	def __next__(self):
		while True:
			try:
				self.current_element = next(self.current_iterator)
				#  пытаемся получить следующий элемент
			except StopIteration:
				if not self.iterators_queue:
						# если в текущем итераторе элементов не осталось и очередь иетраторов пуста
						# завершаем цикл
					raise StopIteration
				else:
						# берем итератор из очереди
					self.current_iterator = self.iterators_queue.pop()
					continue
			if isinstance(self.current_element, list):
					# если следующий эелемент оказался списком, то
					# добавляем текущий итератор в очередь
					# а текущим итераторм делаем следующий элемент
				self.iterators_queue.append(self.current_iterator)
				self.current_iterator = iter(self.current_element)
			else:
					# если элемент не список, то просто возвращаем его
				return self.current_element


for item in SecondIterator(n_list):
	print(item)


def second_generator(some_list):
	for some in some_list:
		if isinstance(some, list):
			yield from second_generator(some)
		else:
			yield some


# for item in second_generator(n_list):
# 	print(item)

