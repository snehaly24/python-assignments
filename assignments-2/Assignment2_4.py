"""
4.Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)
"""

def factorAddition(no):
    res = 0
    
    for i in range(1,int(no/2)+1):
        if(no % i == 0):
            res = res + i
    return res
    
def main():
    no = int(input("Enter number :"))
    res = factorAddition(no)
    print("Factor addition of {} is {}".format(no,res))
        
    
if __name__ == "__main__":
    main()
