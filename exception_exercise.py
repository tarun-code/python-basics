d={1: "red" , 2: "Blue" , 3: "Orange"}

try :
    key=None  
    key=int(input("Enter Your Key: "))
    print(f"the color is :",{d[key]})
    
except ValueError :
          print(f"the  key {key} is not not the valid data typ  ")
          try:
            key=int(input("Enter Your Key again as int : "))         
          except ValueError:
            print(f"i said key {key} is not int type") 
            try:
                key=int(input("Enter Your Key once again as int: "))
            except ValueError:
                print(f"i said key {key} is not int .....tu to rahne de ab")   
      
except KeyError :
       print(f"the  key {key} is not present in dictionary")
       try:
        key=int(input("Enter Your Key again : "))
        print(f"the color is :",{d[key]})
       except KeyError:
            print(f"i said key {key} is not present in dictionary")
            try:
                key=int(input("Enter Your Key once again: "))
                print(f"the color is :",{d[key]})
            except KeyError:
                print(f"i said key {key} is not present .....tu to rahne de ab")  
                
                
                
                
 ##########################################################################################################################               
                
                
                

                
d=[1,2,3,4,5,]

try :
    index=None
    index=int(input("Enter Your index: "))
    print(f"the value is :",{d[index]})
    
except IndexError :
          print(f"the  index {index} is not present in list  ")
          try:
            key=int(input("Enter Your index again  : "))         
          except IndexError:
            print(f"i said index {index} is not in list") 
            try:
                key=int(input("Enter Your index once again : "))
            except IndexError:
                print(f"i said index {index} is not in list .....tu to rahne de ab") 
                
except ValueError :
          print(f"the  index {index} is not not the valid data typ  ")
          try:
            key=int(input("Enter Your index again as int : "))         
          except ValueError:
            print(f"i said index {index} is not int type") 
            try:
                key=int(input("Enter Your index once again as int: "))
            except ValueError:
                print(f"i said index {index} is not int .....tu to rahne de ab")      



#####################################################################################################################

class my_expiry_date(Exception):
    
          pass


try :
    age=None
    age=int(input("Enter Your index: "))
    if age>=100001:
        print("Your life is close to death ")
    else:
        raise my_expiry_date ("you live longer")
       
                
except ValueError :
          print(f"the  age {age} is not not the valid data typ  ")
          try:
            key=int(input("Enter Your age again as int : "))         
          except ValueError:
            print(f"i said age {age} is not int type") 
            try:
                key=int(input("Enter Your age once again as int: "))
            except ValueError:
                print(f"i said age {age} is not int .....tu to rahne de ab")   


####################################################################################################################








                            