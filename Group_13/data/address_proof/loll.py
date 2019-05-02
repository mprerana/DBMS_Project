class node():
	def __init__(self,data):
		self.data = data
		self.next = None	

class linked_list():
	def __init__(self,data):
		self.head = node(data)
	
	def add_node(self,data):
		tmp = self.head
		while tmp.next:
			tmp = tmp.next
		tmp.next = node(data)
	
	def ll_print(self):
		tmp = self
		print(tmp.head.data)
		tmp.head = tmp.head.next
		while tmp.head.next:
			print(tmp.head.data)
			tmp.head = tmp.head.next

	def search3(self):
		tmp = self
		flag = 0
		while tmp.head.next:
			if tmp.head.data == 3:
				print('found')
				flag = 1
				break
			tmp.head = tmp.head.next

		if not flag:
			print('not found')

if __name__=="__main__":
	a = linked_list(10)
	a.add_node(1)
	a.add_node(2)
	a.add_node(3)
	a.add_node(4)
	a.add_node(5)
	a.add_node(6)
#	print(a.ll_print())
	a.search3()