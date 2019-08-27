#Stack class

class Stack:
	
	#constructor
	def __init__(self):
		
		self.items = [] #list of items on the stack 
		self.topIndex = -1 #stores the index of the top of the stack
		
	def push(self, n):
		self.items.append(n)
		self.topIndex = self.topIndex + 1
	
	def pop(self):
		self.topIndex = self.topIndex -1
		return self.items.pop()
	
	def top(self):
		return self.topIndex
	
	def printStack(self):
		for i in self.items:
			print(i)


def main():

	stack = Stack()
	stack.push("Hello")
	stack.push("World") 
	stack.printStack()
	print("Top index = {}".format(stack.top()))
	
if __name__ == '__main__':
	main()

