"""
3. Write a program which accept one number from user and return its factorial.
Input : 5 Output : 120
"""

def factorial(no):
    res = 1
    
    for i in range(1,no+1):
        res = res * i
    return res
    
def main():
    no = int(input("Enter number :"))
    res = factorial(no)
    print("factorial of {} is {}".format(no,res))
        
    
if __name__ == "__main__":
    main()
