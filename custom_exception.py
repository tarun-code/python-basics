
# my custom exception created 
class homogenous_list_error(Exception):
    pass

def value_provider(element):
    datatype_choice = int(input(f"Please choose a datatype of the {element} to be added \
        \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n "))

    if datatype_choice == 1:
        ret_val = int(input("Please enter an integer to be added "))
    elif datatype_choice == 2:
        ret_val = float(input("Please enter a float to be added "))
    elif datatype_choice == 3:
        ret_val = input("Please enter a string to be added ")
    elif datatype_choice == 4:
        ret_val = tuple(input("Please enter a tuple to be added like 1,2 ").split(","))
    elif datatype_choice == 5:
        ret_val = input("Please enter a list to be added like 1,2,3,4 ").split(",")
    elif datatype_choice == 6:
        ret_val = set(input("Please enter a set to be added like 1,2 ").split(","))
    elif datatype_choice == 7:
        my_temp_dict = {}
        keys = input("Please enter the keys of the dictionary to be added like key1,key2 ").split(",")
        for key in keys : 
            
        
            my_temp_dict[key] = value_provider('key'+key)
        ret_val = my_temp_dict
    return ret_val

def create_heterogenous_list(my_list):
    """    3) Create a heterogenous list 
    Note : raise an exception if the users creates a homogenous list (all elements of same datatype)
    """
    for cntr in range(0,int(input("Please enter number of elements to the heterogenous list:::"))):
        my_list.append(value_provider('Index'+str(cntr)))
    print(my_list)   
    
    # check if we are have a homogenous list  
    is_homogenous = True
    for subscript in range(1,len(my_list)):
        if  type(my_list[0]) != type(my_list[subscript]):
            is_homogenous = False
            break
        
    if is_homogenous:
        raise homogenous_list_error
    else:
        print("We received a Heterogenous list ")    
        
my_list = []        
create_heterogenous_list(my_list)