class Pile:
	def __init__(self):
		self.values = []

	def __repr__(self):
		ch = ''
		for x in self.values:
			ch = "|\t" + str(x) + "\t|" + "\n" + ch
		return ch

	def stack(self, value):
		self. values.append(value)

	def unstack(self):
		if self.values:
			return self.values.pop()

	def isEmpty(self):
		return self.values == []