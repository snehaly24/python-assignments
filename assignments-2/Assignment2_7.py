"""
7. Write a program which accept one number and display below pattern.
Input : 5
Output :
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

   
def main():
    no = int(input("Enter number :"))

    for row in range(1,no+1):
        for col in range(1,no+1):
            print(col,end=" ")
        print()
            
if __name__ == "__main__":
    main()
