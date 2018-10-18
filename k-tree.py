class Node:
	def __init__(self, value, father = None):
		self.value = value
		self.father = father
		self.child = []

class Tree:
	def __init__(self, value, qtdChild):
		self.root = Node(value)
		self.qtdChild = qtdChild

	def insert(self, value, current):
		if(len(current.child) == self.qtdChild):
			self.insert(value, current.child[0])
		else:
			current.child.append(Node(value, current))

	def searchPreOrder(self,value, current):
		print(current.value)
		if(current.value == value):
			return True
		else:
			for i in current.child:
				return self.searchPreOrder(value, i) or False


	def searchOrder(self, value, current):
		for i in current.child:
			return self.searchOrder(value, i) or False
		#print(current.value)
		if(current.value == value):
			return True

	def searchPostOrdem(self):
		return True

	#def searchPostOrder(self, value, current):


a = Tree("a",3)
a.insert("b",(a.root))
a.insert("c",(a.root))
a.insert("d",(a.root))
#print(a.root.child[1].value)

print(a.searchOrder("a",(a.root)))