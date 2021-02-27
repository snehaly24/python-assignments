"""
1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
"""
sum = 0
def Addition(arr):
	global sum
	if(len(arr) != 0):
		sum = sum + arr[0]
		print(sum)
		arr.pop(0)
		Addition(arr)
	
	return sum

def main():
	arr = []
	size = int(input("Enter the number of elements :"))
	
	for i in range(size):
		arr.append(int(input("Enter the number :")))
		
	print("Entered data is :",arr)
	
	sum = Addition(arr)
	print("Addition is  : ",sum)
	
if __name__ == "__main__":
	main()