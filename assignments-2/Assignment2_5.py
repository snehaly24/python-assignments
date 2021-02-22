"""
Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number
"""

def prime(no):    
    for i in range(2,int(no/2)+1):
        if(no % i == 0):
            return False
    return True
    
def main():
    no = int(input("Enter number :"))
    res = prime(no)

    if(res == True):
        print("{} is prime number".format(no))
    else:
        print("{} is not prime number".format(no))
            
if __name__ == "__main__":
    main()
