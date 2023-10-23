



# add ,square and exponential

   
def add(num1,num2):
    return num1+num2
def sq(num1):
    return num1*num1
def expo (num1,num2):
    return num1**num2
 
 





def calculator():
    while True:
        
        
            
        print("*****************Welcome to Calculator****************")
        print("press 1 for Addition") 
        print("press 2 for Square")
        print("press 3 for Exponential")
        print("press 4 for Exit")
        opr=int(input("Enter your choice: "))
            
        if opr==1:
                num1=int(input("Enter first number:"))
                num2=int(input("Enter second number:"))
                print(f"Additin of {num1} and {num2} is: ", add(num1,num2) )
            
            
        if opr==2:
                num1=int(input("Enter a number:"))
                print(f"Square of {num1} is: ", sq(num1) )
                
        if opr==3:
                num1=int(input("Enter a number:"))
                num2=int(input("Enter a power:"))
                print(f" exponenation of {num1} power {num2} is: ", expo(num1,num2) )
        if opr==4:
            print("you are exit now...")
            break       
                
                
         
         
                
calculator()               
