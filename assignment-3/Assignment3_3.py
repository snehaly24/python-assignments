"""
3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
"""

def Min(arr):
	min = arr[0]
	for i in range(1,len(arr)):
		if min > arr[i]:
			min = arr[i]
	return min

def main():
	arr = []
	size = int(input("Enter the number of elements :"))
	
	for i in range(size):
		arr.append(int(input("Enter the number :")))
		
	print("Entered data is :",arr)
	
	res = Min(arr)
	print("Minimum number is  : ",res)
	
if __name__ == "__main__":
	main()