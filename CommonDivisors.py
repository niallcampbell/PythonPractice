# Common divisors

# Given two numbers entered by the user, return: 1. number of common divisors, 2. a list of the common divisors

def commonDivisors():
	
	print("Please enter two numbers separated by a single space")
	print("For example: 2 10")
	print()

	rawNumbers = input("Your numbers: ")
	
	listNumbers = rawNumbers.split(" ")
	
	a = int(listNumbers[0])
	b = int(listNumbers[1])
	
	n = 0
	
	for i in range(1, min(a,b)+1):
		if(a%i==0 and b%i==0):
			
			if(n == 0):
				print("Divisors: " + repr(i), end="")
				n+=1
			else:
				print(", " + repr(i), end="")
				n+=1
	
	print()
	print("Number of divisors: " + repr(n))
	
	
def main():
	
	commonDivisors()

if __name__ == '__main__':
	main()

