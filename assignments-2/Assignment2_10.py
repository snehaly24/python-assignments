"""
Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37
"""

   
def main():
    no = int(input("Enter number :"))

    sum = 0
    while(no != 0):
        sum = sum + (no % 10)
        no = no // 10
        
    print("Length :",sum)
            
if __name__ == "__main__":
    main()
