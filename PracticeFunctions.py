#Python function practice

#reverse integer
def reverseInt():
	
	n = int(input("Please enter a number to be reversed: "))
	
	r = 0
	
	while (n > 0):
		
		temp = n % 10
		r = (r * 10) + temp
		n = int(n / 10)
	
	print(r)


#Given two strings, get the characters common to both.  
def commonCharacters(a, b):
	
	al = len(a)
	bl = len(b)
	
	listChars = []
	
	for i in a:
		for j in b:
			if(i == j):
				listChars.append(i)
	
	for x in listChars:
		print(x, end=" ")



def main():
	
	#reverseInt()
	commonCharacters("abcd", "eafd")


if __name__ == '__main__':
	main()