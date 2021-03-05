"""
3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
"""

class Arithmetic():
		
	def __init__(self,value1=0,value2=0):
		self.value1 = 0
		self.value2 = 0
				
	def Accept(self):
		self.value1 = int(input("Enter the first number :"))
		self.value2 = int(input("Enter the second number :"))
		
	def Addition(self):
		return self.value1 + self.value2
	
	def Subtraction(self):
		return self.value1 - self.value2
	
	def Multiplication(self):
		return self.value1 * self.value2
		
	def Division(self):
		return self.value1 / self.value2
		
def main():
	
	Obj1 = Arithmetic()
	Obj1.Accept()
	
	print("Addition is :",Obj1.Addition())
	print("Subtraction is :",Obj1.Subtraction())
	print("Multiplication is :",Obj1.Multiplication())
	print("Division is :",Obj1.Division())
	
	Obj2 = Arithmetic()
	Obj2.Accept()
	print("Addition is :",Obj2.Addition())
	print("Subtraction is :",Obj2.Subtraction())
	print("Multiplication is :",Obj2.Multiplication())
	print("Division is :",Obj2.Division())
	
if __name__ == "__main__":
	main()