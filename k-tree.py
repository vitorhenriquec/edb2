class Node:
	def __init__(self, value):
		self.value = value
		self.child = []

class Tree:
	def __init__(self, value, qtdChild):
		self.root = Node(value)
		self.qtdChild = qtdChild

	def insert(self, value, current):
		if(len(current.child) == self.qtdChild):
			self.insert(value)
		else:
			current.child.append(Node(value))

	def searchPreOrder(self,value, current):
		'''print(current.value)
		print("\n")'''
		if(current.value == value):
			return current
		else:
			for i in current.child:
				self.searchPreOrder(value, i)
			

	def searchPostOrder(self, value, current):
		for i in current.child:
			self.searchPostOrder(value, i)

		'''print(current.value)
		print("\n")'''
		if(current.value == value):
				return current
		else:
			return None


	def searchOrder(self, value, current):
		if current.child:
			for i in current.child:
				self.searchPostOrder(value, i)
		else:
			if current.value == value:
				return current
			else:
				return

	def remove(self, value, current):
		tmp = self.searchPreOrder(value, current)
		if tmp != None:
			if len(tmp.child) > 0:
				tmp.value = tmp.child[0].value
				for i in tmp.child[0].child:
					i.father = aux
				tmp.child += tmp.child[0].child
				tmp.child.pop(0)


a = Tree("a",3)
a.insert("b",(a.root))
a.insert("c",(a.root))
a.insert("d",(a.root))
a.insert("k",(a.root))
a.insert("f",(a.root))
a.insert("p",(a.root))
#print(a.root.child[1].value)

print(a.searchPreOrder("p",(a.root)))