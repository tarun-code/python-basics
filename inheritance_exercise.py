

class Employee:
    organisation_name = "GOOGLE"  # Class variable

    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.deployed_location = deployed_location
        self.designation = designation
        self.salary = salary

    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}"

    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name

    @classmethod
    def set_organisation_name(cls, org_name):
        cls.organisation_name = org_name


class Manager(Employee):
    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        super().__init__(emp_id, name, base_location, deployed_location, designation, salary)
        self.managed_employees = []  # List to store managed employees

    def perform_appraisal_for_an_employee(self, emp_id, percent_raise):
        for employee in self.managed_employees:
            if employee.emp_id == emp_id:
                employee.salary *= (1 + percent_raise / 100)

    def get_manager_details(self, mgr_id):
        return self.get_employee_details() + f", Managed Employees: {len(self.managed_employees)}"


def main():
    # Create three Employee objects
    emp1 = Employee(101, "tarun", "HQ", "Branch 1", "boss", 10000)
    emp2 = Employee(102, "trishna", "HQ", "Branch 2", "developer", 70000)
    emp3 = Employee(103, "sushmita", "HQ", "Branch 3", "admin Enggineer", 65000)

    # Create a Manager object and add the Employee objects as managed employees
    manager = Manager(201, "shruti", "HQ", "Branch 1", "Manager", 80000)
    manager.managed_employees.extend([emp1, emp2, emp3])

    # Display manager details
    print(manager.get_manager_details(201))

    # Perform appraisal for an employee (e.g., 101) under the manager
    manager.perform_appraisal_for_an_employee(101, 10)
    print("After Appraisal:")
    for emp in manager.managed_employees:
        print(emp.get_employee_details())

if __name__ == "__main__":
    main()
