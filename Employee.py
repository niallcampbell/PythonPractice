#Employee class / object

class Employee:
	
	'Base Class for Employee Objects'
	
	#class variables
	company = "GloboCorp"
	location = "Dublin"
	
	#constructor
	def __init__(self, name, age, salary):
		
		#instance variables
		self.name = name
		self.age = age
		self.salary = salary
		
	def setSalary(self, newSalary):
		
		self.salary = newSalary
		
	def getSalary(self):
	
		return self.salary
		
	def printDetails(self):
		
		print("Name: {}".format(self.name))
		print("Age: {}".format(self.age))
		print("Salary: {}".format(self.salary))
		

#Inherits Employee Class
class Developer(Employee):
	
	job = "Developer"
	
	def __init__(self, name, age, salary, skills):
		
		#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
		Employee.__init__(self, name, age, salary)
		self.skills = skills
		
	
	def printDetails(self):
		
		print("Name: {}".format(self.name))
		print("Age: {}".format(self.age))
		print("Salary: {}".format(self.salary))
		print("Job: {}".format(self.job))
		
		#print skills
		print("Skills: ", end = " ")
		l = len(self.skills)
		
		for i in self.skills:
			print(i, end = " ")


def main():
	
	emp = Employee("Niall", 25, 30000)
	emp.printDetails()
	
	print()
	
	dev = Developer("Alan", 27, 35000, ["Java", "Python"])
	dev.printDetails()
		
	
if __name__ == '__main__':
	main()