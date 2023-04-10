operations=["+","-","/","*","%","q"]

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

    print("<<CALCULATER>>")
    num1=float(input("Please enter first number:"))
    num2=float(input("Please enter second number:"))
    print("If you want to exit from calculator, please press 'q'!")
    operation=input("Select your operation (+,-,/,*,%,q):")
    if operation!=operations:
       print("Plese enter a valid operation!")
   

    if operation=="q":
       break

    if operation=="+":
       print("The result of add operation is:",add(num1,num2))
    elif operation=="-":
         print("The result of subs operation is:",subs(num1,num2))
    elif operation=="/":
        if num2==0:
           print("A number does not dived by 0!")
        else:
            print("The result of divide operation is:",divide(num1,num2))    
    elif operation=="*":
         print("The result of multiply operation is:",multiply(num1,num2))
    elif operation=="%":
         print("The result of mod operation is:",mod(num1,num2))
         continue  
     

   
