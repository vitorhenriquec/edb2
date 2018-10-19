class Node:
	def __init__(self, **kwargs):
		self.value = kwargs.get('value')
		self.children = []

class kAryTree:
	def __init__(self, value):
		self.root = Node(value)

	def insert(self, value):
		self.__insertValues(value, self.root)

	def __insertValues(self, value, current):
		if not value:
			return
		if current and not current.value:
			tmp = None

			for child in current.children:
				if value[0] == child.value:
					tmp = child
					break

			if tmp:
				self.__insertValues(value,tmp)
			else:
				nNode= Node(value = data[0])
				current.children.append(nNode)
				self.__insertValues(data, nNode)
		else:
			if len(value) > 1
				tmp = None
				for child in current.children:
					if value[1] == child.value:
						tmp = child
						break

				if tmp:
					self.__insertValues(value[1:],tmp)
				else:
					nNode = Node(value=data[1])
					current.children.append(nNode)
					self.__insertValues(data[1:], nNode)
	def search(self, ):

