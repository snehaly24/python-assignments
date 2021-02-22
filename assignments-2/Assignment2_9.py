"""
Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7
"""

   
def main():
    no = int(input("Enter number :"))

    len = 0
    while(no != 0):
        no = no // 10
        len = len + 1

    print("Length :",len)
            
if __name__ == "__main__":
    main()
