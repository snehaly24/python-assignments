"""
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division.
All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by
accepting the parameters from user
"""

import Arithmetic as AR

def main():
    no1 = int(input("Enter first number :"))
    no2 = int(input("Enter second number :"))

    add = AR.Add(no1,no2)
    sub = AR.Sub(no1,no2)
    mul = AR.Mult(no1,no2)
    div = AR.Div(no1,no2)

    print("Addition is :",add)
    print("Substraction is :",sub)
    print("Multipllication is :",mul)
    print("Division is :",div)

        
    
if __name__ == "__main__":
    main()
