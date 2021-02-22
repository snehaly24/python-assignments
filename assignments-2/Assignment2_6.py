"""
6. Write a program which accept one number and display below pattern.
Input : 5
Output :
* * * * *
* * * *
* * *
* *
*
"""

   
def main():
    no = int(input("Enter number :"))

    for row in range(no,0,-1):
        for col in range(row):
            print("*",end=" ")
        print()
            
if __name__ == "__main__":
    main()
