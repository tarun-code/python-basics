def list_display_members(members) :
    return len(members)

def list_add_element(members) :
	return members.append(members)

def list_add_elements(members):
	return members.extend([members])

def list_remove_element(members,member) :
    return members.remove(member)

def remove_last_element(members) :
	return members.pop()

def display_3_4_5_element(members):
	return members[2],members[3],members[4]


def my_list_store():
    print("\n Welcome to Our List Store !!! ")
    # print("Please enter a list Comma seperated that you would want to perform Operation Upon")
    # members = input('for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania \n:::').split(",")
    members=[None]
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display number of elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice :"))
        
        if choice   ==1:
            print("members are:",list_display_members(members)) 
        elif choice ==2:
         
             print("Please Enter a member")
             members = input('for ex: Pratiksha \n:::').split(",")
             list_add_element(members) 
             print("Element aadded in list")
        elif choice ==3:
         
            print("Please enter a list Comma seperated that you would want to perform Operation Upon")
            members = input('for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania \n:::').split(",")
        
            list_add_elements(members)
            print("Elements are aadded in list")
        elif choice ==4:
            member = input('Enter a Element \n:::')
            list_remove_element(members,member) 
            print("Element Removed ")
        elif choice ==5:
            remove_last_element(members) 
            print("Last Element Removed ")
        elif choice ==6:
            if len(members)>6:
               print("Members 3,4,5 Are:",display_3_4_5_element(members))
            else:
                print("Members are less then 5")
                    
        elif choice ==7:
            print("exiting..........")
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")


my_list_store()	            