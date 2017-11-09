from node import Node

class input(Node):
	"""docstring for input"""

	id = 0;

	def __init__(self, name, id, targets = None):
		global id
		super().__init__(name, 'I' + str(id))
		id += 1
		if targets not in None:
			for t in targets:
				self.targets.add(t)
		