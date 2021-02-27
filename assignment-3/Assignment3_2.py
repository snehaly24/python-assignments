"""
2.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
"""

def Max(arr):
	max = arr[0]
	for i in range(1,len(arr)):
		if max < arr[i]:
			max = arr[i]
	return max

def main():
	arr = []
	size = int(input("Enter the number of elements :"))
	
	for i in range(size):
		arr.append(int(input("Enter the number :")))
		
	print("Entered data is :",arr)
	
	res = Max(arr)
	print("Maximum number is  : ",res)
	
if __name__ == "__main__":
	main()