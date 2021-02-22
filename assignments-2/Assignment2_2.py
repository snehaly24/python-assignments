"""
Write a program which accept one number and display below pattern.
Input : 5
Output :
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

def main():
    no = int(input("Enter number :"))

    for row in range(no):
        for col in range(no):
            print("*",end = " ")
        print("")
        
    
if __name__ == "__main__":
    main()
