#Queue class

#Queue is FIFO
#items are inserted at the rear of the queue (end of the list) and removed from the front (start of the list)

class Queue:

	def __init__(self, size):
		
		self.size = size # max allowed size of the queue
		self.items = [None] * size
		self.front = 0
		self.rear = -1
		self.numItems = 0 #number of items in the queue
		
	def isEmpty(self):
	
		if(self.numItems == 0):
			return true
		else:
			return false
	
	#Inserts items at the rear of the queue
	def insert(self, n):
		
		if(self.numItems == self.size):
			print("Queue is full")
			return
		else:
			#wrap rear back to the start of the list should you reach the end of the list
			if(self.rear == self.size - 1):
				self.rear = - 1
			
			self.rear+=1
			self.items[self.rear] = n
			self.numItems+=1
			print("Insert item: {}".format(n))
	
	#remove item from the front of the queue
	def remove(self):
		
		print("Removing item: {}".format(self.items[self.front]))
		
		self.front+=1
		
		if(self.front == self.size):
			self.front = 0
		
		self.numItems-=1
		
	
	#return the number of items in the queue
	def getSize(self):
		
		return self.numItems
	
	
	def printQueue(self):
		
		if(self.front <= self.rear):
			
			for i in range(self.front, self.rear + 1):
				print(self.items[i], end = " ")
		
		# there has been a wrap around
		elif(self.front > self.rear):
			
			#Print from the front to the end of the list
			for i in range(self.front, self.size):
				print(self.items[i], end=" ")
				
			#Print from the beginning of the list to the rear
			for i in range(0, self.rear + 1):
				print(self.items[i], end=" ")
		
		print()
		
		
def main():

	q = Queue(3)
	q.insert(1)
	q.insert(2)
	q.insert(3)
	q.printQueue()
	q.remove()
	q.printQueue()
	q.insert(4)
	q.printQueue()

if __name__ == '__main__':
	main()
			
	