
def data_store_Dictonary():
 
        


    dictionary={}
    while True:
        print("\n*************** Menu **********************")
        print("Enter a data type you want :")
        print("  1: for integer")
        print("  2: for string ")
        print("  3: for tuple ")
        print("  4: for float value")
        print("  5: for set ")
        print("  6: for List")
        print("  7: Dispaly the Dictionary ")
        print("  8: Exit the Program ")
        
        choice = int(input("Please enter your choice :"))
        if choice==1:
            key_num =input("Enter a key :") 
            val_num =input("Enter a data :")
            if val_num.isdigit():
            
                val_num=int(val_num) 
                if type(val_num)==int:
                 dictionary[key_num] = val_num
                 print("Added To The Dictionary")
                else:
                 print("you entered Wrong data type!!") 
            else:
                print("you entered Wrong data type!!")          
            
            
        elif choice==2:
            key_str =input("Enter a key :") 
            val_str =(input("Enter a data :") )
            if  not val_str.isdigit():
                val_str=str(val_str)
                if type(val_str)==str:
                 dictionary[key_str] = val_str
                 print("Added To The Dictionary")
                
                else:
                 print("you entered Wrong data type!!")
            else:
                print("you entered Wrong data type!!")  
        elif choice==3:
            key_tuple =input("Enter a key :") 
            val_tuple =(input("Enter a data like tarun,trishna :") ).split(",")
            val_tuple=tuple(val_tuple)
            if type(val_tuple)==tuple: 
              dictionary[key_tuple] = val_tuple
              print("Added To The Dictionary")
            else:
              print("you entered Wrong data type!!")
            
        elif choice==4:
            key_float =input("Enter a key :") 
            val_float =(input("Enter a data in float :") )
            val_float=float(val_float)
            if type(val_float)==float: 
              dictionary[key_float] = val_float
              print("Added To The Dictionary")
            else:
              print("you entered Wrong data type!!")
            
        elif choice==5:
            key_set =input("Enter a key :")  
            val_set =(input("Enter a data like tarun,trishna :") ).split(",")
            val_set=set(val_set)
            if type(val_set)==set:  
             dictionary[key_set] = val_set
             print("Added To The Dictionary")
            else:
              print("you entered Wrong data type!!")
            
        elif choice==6:
                
                key_list =input("Enter a key :")  
                val_list =(input("Enter a data like trishna,tarun :") ).split(",")
                val_list=list(val_list)
                if type(val_list)==list: 
                  dictionary[key_list] = val_list
                  print(f"Added To The Dictionary!!")
                
                else :
        
                 print("you entered Wrong data type!!!!!") 
                 
                 
                 
        elif choice==7:
            print(dictionary)
            # val=dictionary.keys()
            # val2=dictionary.values()
            # print(val)  
            # print(val2)  
                                        
        elif choice==8:
            print("you are Exit now..........") 
            break
        
        else:
            print("you entered Wrong choice!!")
            
            
            
            
            
            
            
            
            
            
            
data_store_Dictonary()            