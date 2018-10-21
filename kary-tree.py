class Node:
	#__value = torna value privado
	def __init__(self, value, father=None, lChild=None, rSibiling=None):
		self.value = value
		self.father = father
		self.lChild = lChild
		self.rSibiling = rSibiling
		self.qtdChild = 0

class kAryTree:
	def __init__(self, value, treetype):
		self.root = Node(value)
		self.treetype = treetype

	def insert(self, value, father):
		aux = self.searchPreOrder(father,self.root)
		if aux != None:
			if aux.qtdChild < self.treetype:
				if aux.lChild == None:
					aux.lChild = Node(value, aux)
					aux.qtdChild+=1
				else:
					if aux.lChild.rSibiling != None :
						tmp = aux.lChild.rSibiling
						while (tmp.rSibiling != None):
							tmp = tmp.rSibiling
						tmp.rSibiling = Node(value, aux)
					else:
						aux.lChild.rSibiling = Node(value, aux)
					aux.qtdChild+=1
			else:
				print("Impossivel adicionar")
		else:
			print("Pai nao encontrado")	

	def search(self,value,tipo=1):
		aux = None
		if tipo == 1:
			return self.searchPreOrder(value,self.root)
		elif tipo == 2:
			return self.searchOrder(value, self.root)
		elif tipo == 3:
			self.searchPostOrder(value, self.root)
			return aux


	def searchPreOrder(self,value,current):
		if current.value == value: 
			return current
		else:
			if current.lChild != None:
				return self.searchPreOrder(value,current.lChild)
			while(current.rSibiling != None):
				return self.searchPreOrder(value,current.rSibiling)			

	def searchPostOrder(self,value,current):
		if current.lChild != None:
			return self.searchPostOrder(value,current.lChild)
			while(current.rSibiling != None):
				return self.searchPostOrder(value,current.rSibiling)
		elif(current.value == value):
			return current

	def searchOrder(self,value,current):
		if current.lChild != None:
				return self.searchOrder(value,current.lChild)
		else:
			if(current.value == value):
				return current	
			while(current.rSibiling != None):
				return self.searchOrder(value,current.rSibiling)
		
	def remove(self, value):
		__remove(value,self.root)

	def __remove(self, value, current):
		tmp = self.searchPreOrder(value, current)
		if tmp != None:
			children = []
			if tmp.lChild != None:
				if tmp.lChild.rSibiling != None:
					tmp1 = tmp.lChild.rSibiling 
					tmp.value = tmp.lChild.value
					tmp.lChild = tmp.lChild.lChild
					tmp2 = tmp.lChild.rSibiling
					while (tmp2.rSibiling != None):
							tmp2 = tmp2.rSibiling
					tmp2.rSibiling = tmp1
				else:
					tmp= tmp.lChild
			elif tmp.rSibiling == None:
				del tmp
		else:
			print("Impossivel remover")

a = kAryTree("a",3)
a.insert("b","a")
a.insert("c","a")
a.insert("d","a")
a.insert("k","d")
print("Type of search: 1 - PreOrder \t 2 - Order\t 3 - PostOrder")
print(a.search("k",int(input())) != None)