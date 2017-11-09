from node import Node

class input(Node):
	"""docstring for input"""

	id = 0

	def __init__(self, name, id, targets = None, order = 20, general_para = 0.001):
		global id
		super().__init__(name, 'I' + str(id))
		id += 1
		if targets not in None:
			for t in targets:
				self.targets.add(t)
		self.input = 0
		#function: (power, parameter)
		self.function = set()
		for i in range(order):
			self.function.add((i, general_para))
		self.result = 0
	
	def add_target(self, ref):
		super().add_target(ref)

	def calc_result(self, input):
		self.result = 0
		for pair in self.function:
			self.result += input ** pair[0] * pair[1]