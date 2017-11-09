from exceptions import *

class Node:
	def __init__(self, name = None, id = 0):
		self.name = name
		self.id = id
		self.parents = set()
		self.targets = set()

	def add_target(self, ref):
		if ref not in self.targets:
			self.targets.add(ref)
		else:
			raise addTargetError("adding an existing target {} to {}".format(self.id, ref.id))


	def add_parent(self, ref):
		if ref not in self.parents:
			self.parents.add(ref)
		else:
			raise addTargetError("adding an existing parent {} to {}".format(self.id, ref.id))