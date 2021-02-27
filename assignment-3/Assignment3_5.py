"""
5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5)
"""
import MarvellousNum

def main():
	arr = []
	brr = []
	
	size = int(input("Enter the number of elements :"))	
	
	for i in range(size):
		arr.append(int(input("Enter the number :")))
		
	print("Entered data is :",arr)
	
	sum = 0
	for i in range(size):
		res = MarvellousNum.ChkPrime(arr[i])
		if res == True:
			brr.append(arr[i])
			sum = sum + arr[i]
	
	print(brr)
	print("sum of prime numbers :",sum)
	
if __name__ == "__main__":
	main()