# Exercise on Inheritance:
# -------------------------
# Create a base class named Employee as follows:
# Employee (
# -- class variables and methods
# 	organisation_name, 
# 	get_organisation_name(),
# 	set_organisation_name(org_name)

# -- instance variables and methods()
# emp_id,
# name,
# base_location,
# deployed_location,
# designation,
# salary ,
# get_employee_details() 	


# Create a subclass of Employee named Manager as follows:
# Manager(
	
# 	-- instance variables and methods()
# 	managed_employees[],
# 	perform_appraisal_for_an_employee(emp_id,percent_raise),
# 	get_manager_details(mgr_id)
# )

# Write a main method that does the following:
# create 3 objects of Employee 
# create an object of Manager_class and add the above 3 employee objects created as managed employees 
# display get_manager_details()
# for an employee do perform_appraisal_for_an_employee()



class Employee:
    
    
    organisation_name="Cdac"
    
    
    @classmethod
    def get_organisation_name(cls):
       return cls.organisation_name        
    def set_organisation_name(cls,rec_name):
        cls.organisation_name=rec_name
        
    
    def __init__(self,id,salary,mgr_id,base_loc,name,dep_location,design) :
        
      self.emp_id=id
      self.emp_salary=salary
      self.mgr_id=mgr_id
      self.base_location=base_loc
      self.name=name
      self.dep_loc=dep_location
      self.designation=design
      
    
    
    
    
    def get_employee_details(self):
      return print(self.emp_id and
      self.emp_salary and
      self.mgr_id and
      self.base_location and
      self.name and
      self.dep_loc and
      self.designation)
      
        
        
        
        
        
        
    def get_emp_salary(self):
        return self.emp_salary
    
    def set_emp_salary(self,new_salary):
        
        self.emp_salary=new_salary
    
    
  
   
    @staticmethod
    def field_expertise():
        return "Expertise are : java python mongodb\n"
          
def main():
    
    
     tarun= Employee(1,2000,100,"raipur","tarun","pune","developer")
     trishna= Employee(2,3000,200,"delhi","trishna","banglore","admin")
     
 

     
     
     
     
 
    
    
if __name__ == "__main__":
    main()   