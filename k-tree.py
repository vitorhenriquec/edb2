'''
	Made by Vitor Henrique (github.com/vitorhenriquec)
'''

class Node:
	def __init__(self, value, father=None):
		self.value = value
		self.father = father
		self.child = []

class Tree:
	def __init__(self, value, qtdChildren=1):
		self.root = Node(value)
		self.qtdChildren = qtdChildren

	def insert(self, value):
		def __insert(value, current):
			if(len(current.child) == self.qtdChildren):
				__insert(value, current.child[0])
			else:
				current.child.append(Node(value, current))
		__insert(value,self.root)

	def search(self,value,typeS=1):
		def __searchPreOrder(value, current):
			if(current.value == value):
				return current
			for i in current.child:
				aux =__searchPostOrder(value, i)
				if aux != None:
					return aux

		def __searchPostOrder( value, current):
			for i in current.child:
				aux = __searchPostOrder(value, i)
				if aux != None:
					return aux
			if(current.value == value):
				return current

		def __searchOrder(value, current):
			for i in current.child:
				aux = __searchPostOrder(value, i)
				if aux != None:
					return aux
				if current.value == value:
					return current
			

		if typeS ==1: 
			return __searchPreOrder(value,self.root)
		elif typeS == 2: 
			return __searchOrder(value,self.root)
		elif typeS == 3:
			return __searchPostOrder(value,self.root)


	def remove(self,value):
		def __remove(value, current):
			tmp = self.search(value,1)
			if tmp != None:
				if len(tmp.child) != 0:
					tmp.value = tmp.child[0].value
					for i in tmp.child[0].child:
						i.father = tmp
					tmp.child += tmp.child[0].child
					tmp.child.pop(0)
				else:
					if tmp.father != None:
						tmp.father.child.remove(tmp)
			else:
				print("Value {} not found.Can't delete".format(value))
		__remove(value,self.root)

def __main__():
	qtdChildrenren = int(input("N of children:\n"))
	root = str(input("Root value:\n"))
	tree = Tree(root,3)
	op = -1
	while(op !=0):
		op = int(input("ACTION:\n1 - ADD \n 2 - SEARCH \n 3 - REMOVE \n 0 - EXIT\n"))
		if op ==1:
			tree.insert(input("Value: \n"))
		elif op ==2:
			typeSearch = int(input("Type of search:\n 1 - PreOrder \n 2- Order \n 3- PostOrder\n"))
			print("Not Found\n") if(tree.search(str(input("Value:\n")),typeSearch)==None) else print("Found\n")
		elif op ==3:
			tree.remove(str(input("Value:  ")))
__main__()