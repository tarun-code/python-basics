import module_functions1 as m


def opr1():
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    print("the sum is :",m.addition(num1,num2))
    print("the square is :",m.square(num1))
    print("the raised is :",m.Raised(num1,num2))


def upr():
  str=input("enter a string:")
  print("string is converted into uppercase:",m.uppercase(str))



def raisedsal ():
      raise_salary_percentage=int(input("enter the raised percentage:"))
      name =input("enter the username:")
      existing_salary = int(input("enter the existing salary:"))
      print(name," salary raised by:",m.raised_sal(existing_salary,raise_salary_percentage))


def heigh():
    height=int(input("enter the height in cm:"))
    print("height in feet is :",m.foot(height))
    print("height in inches is :",m.inch(height))


def dollr():
    
    doller=int(input("enter the amount in doller:"))
    print(doller,"$ in INR is :",m.doller(doller))



def disc():
    discount_percentage=int(input("enter the discount percentage:"))
    source=input("enter the source:")
    destination=input("enter the destination:")
    fare=int(input("enter the fare:"))
    print (fare,"is a fare of" ,source ,"to ",destination," and discount is :",m.discount(discount_percentage,fare)," rs and discount percentage is ",discount_percentage, " and payable amount is :",fare-m.discount(discount_percentage,fare))

disc()
dollr()
heigh()
raisedsal ()
upr()
opr1()





