class error(Exception):
	pass

class addTargetError(error):

	def __init__(self, message):
		self.message = message