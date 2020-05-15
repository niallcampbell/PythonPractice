# Link for a LinkedList

class Link:
	
	def __init__(self, name, age):
	
		#instance variables
		self.name = name
		self.age = age
		self.next = None
		
	def printLink(self):
		print("Name: {}".format(self.name))
		print("Age: {}".format(self.age))
		print()
		
	def compareLinks(self, other):
		if ((self.name == other.name) and (self.age == other.age)):
			return True
		else:
			return False
		
	
class LinkedList():
	
	def __init__(self):
		self.head = None
		
	def printList(self):
		n = self.numLinks()
		print("Number of Links: {}".format(n))
		print()
		val = self.head
		while val is not None:
			val.printLink()
			val = val.next
			
	def numLinks(self):
		n = 0
		val = self.head
		while val is not None:
			n = n + 1
			val = val.next
		return n 
	
	# insert link at the end of the list
	def insertLink(self, newLink):
		val = self.head
		
		if val is None:
			self.head = newLink
			return
		
		while val.next is not None:
			val = val.next
			
		val.next = newLink
		
	def removeLink(self, node):
		if node is None:
			return
		
		prev = self.head
		
		# if we are deleting the head
		if (prev.compareLinks(node)):
			print("Removing link: {}".format(node.name))
			print()
			self.head = prev.next
			return
		
		current = prev.next
		
		while current is not None:
			if (current.compareLinks(node)):
				print("Removing link: {}".format(node.name))
				print()
				prev.next = current.next
				return
			else:
				prev = current
				current = current.next
		
	

class main():

	# create new empty LinkedList
	myList = LinkedList()
	
	link1 = Link("niall", 25)
	
	myList.insertLink(link1)
	
	link2 = Link("sean", 33)
	
	myList.insertLink(link2)
	
	link3 = Link("james", 42)
	
	myList.insertLink(link3)
	
	link4 = Link("paul", 34)
	
	myList.insertLink(link4)
	
	myList.printList()
	
	myList.removeLink(link3)
	myList.removeLink(link1)
	myList.removeLink(link4)
	myList.removeLink(link2)
	
	myList.printList()
	

# use main class by default

if __name__ == '__main__':
	main()
	