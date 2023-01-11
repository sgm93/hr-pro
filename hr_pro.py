class Employee:
    def __init__(self,name,age,salary,years):
        self.name=name
        self.age=age
        self.salary=salary
        self.employment_years=years
    def get_annual_salary(self,salary): 
        return self.salary*12 
    def __repr__(self):
        return f"the name is :{self.name},the age is :{self.age},the salary is:{self.salary}, the employment years are :{self.employment_years}"      

class Manager(Employee):
    def __init__(self,name,age,salary,years,bonus_percentage):
        super().__init__(name,age,salary,years)
        self.bonus_percentage=bonus_percentage
    def get_bonus(self,bonus_percentage,salary):
        return self.bonus_percentage*self.salary
    #Manager class here
    def __repr__(self):
      return f"{super().str()} ,the bonus percentage is :{self.bounas_percentage} "  
        
def main():
	# main code here
    employee1=Employee("sara",29,800,6)
    employees=[employee1]
    managers=[Manager("sara",29,800,6,10)]
    option=input("Options:1. Show Employees 2. Show Managers 3. Add An Employee 4. Add A Manager 5. Exit hat would you like to do?")
    while option!="5":
        if option=="1":
         print(employees)
        elif option=="2":
         print(managers)
        elif option=="3":
            name=input("name:")
            age=input("age:")
            salary=input("salary:")
            employment_years=input("employment years:")
            employees.append(Employee(name,age,salary,employment_years))
            print("Employee added succesfully")
        elif option=="4":
            name=input("name:")
            age=input("age:")
            salary=input("salary:")
            employment_years=input("employment years:")
            managers.append(Manager(name,age,salary,employment_years))
            print("Employee added succesfully")

        exit()
    







if __name__ == '__main__':
	main()
