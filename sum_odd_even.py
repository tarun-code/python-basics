
 
 # sum ,odd,even number 
 
 
def sum():
  num3=int(input("Enter a number:")) 
  sum=0
  i=1
  while i<=num3:
      sum=sum+i
      i+=1
  print("Sum is :",sum)    
  
def odd():
    num=int(input("Enter a number:"))
    list1=list(range(1,num+1,2))
    for i in list1:
     print(i)
   
def even():  
    num2=int(input("Enter a number:"))
    list2=list(range(2,num2+1,2))
    for i in list2:
     print(i)
 

   
sum()
even()
odd()
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
