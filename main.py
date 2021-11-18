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
		self.some_list = sum(some_list, start=[])

	def __iter__(self):
		self.counter = -1
		return self

	def __next__(self):
		self.counter += 1
		if self.counter == len(self.some_list):
			raise StopIteration
		return self.some_list[self.counter]


# for item in FirstIterator(nested_list):
# 	print(item)


class SecondIterator():
	def __init__(self, some_list):
		self.some_list = sum(some_list, start=[])

	def __iter__(self):
		self.counter = -1
		return self

	def __next__(self):
		if isinstance(self.some_list, list):
			self.counter += 1
			if self.counter == len(self.some_list):
				raise StopIteration
			return self.some_list[self.counter]


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

