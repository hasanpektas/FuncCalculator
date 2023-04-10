print("Calculator")
operations=["+","-","/","*","%","q"]

def getnumbers():
    num1=float(input("Please enter first number:"))
    num2=float(input("Please enter second number:"))
    return num1,num2

def getoperations():
    operation=input("Select your operator (+,-,/,*,%,q):")
    if operation in operations:
        return operation
    else:
        print("Plese give a valid operator")

def add(num1,num2):
    return num1+num2
def subs(num1,num2):
    return num1-num2
def divide(num1,num2):
    return num1/num2
def multiply(num1,num2):
    return num1*num2
def mod(num1,num2):
    return num1%num2

while True:
    
    num1,num2=getnumbers()
    print("If you want to exit from calculator, please press 'q'!")
    operation=getoperations()
   

    if operation=="q":
        break

    if operation=="+":
        print("The result is:",add(num1,num2))
    elif operation=="-":
        print("The result is:",subs(num1,num2))
    elif operation=="/":
        if num2==0:
            print("A number not dived by 0")
        else:
            print("The result is:",divide(num1,num2))    
    elif operation=="*":
        print("The result is:",multiply(num1,num2))
    elif operation=="%":
        print("The result is:",mod(num1,num2))
        continue
     

   
