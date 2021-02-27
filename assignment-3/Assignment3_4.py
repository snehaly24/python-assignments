"""
4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
"""

def Frequency(arr,no):
	freq = 0
	for i in range(len(arr)):
		if no == arr[i]:
			freq = freq + 1
	return freq

def main():
	arr = []
	size = int(input("Enter the number of elements :"))	
	for i in range(size):
		arr.append(int(input("Enter the number :")))
		
	no = int(input("Enter the number to search : "))		
	print("Entered data is :",arr)
	
	res = Frequency(arr,no)
	print("{} found {} times".format(no,res))
	
if __name__ == "__main__":
	main()