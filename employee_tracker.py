import os
from tabulate import tabulate
from colorama import Fore, Style

class Employee:
    def __init__(self, emp_id, name, designation, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} | {self.name} | {self.designation} | {self.department} | {self.salary}"

def load_employees(filename="employees.txt"):
    employees = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                emp_id, name, designation, department, salary = line.strip().split(",")
                employees.append(Employee(emp_id, name, designation, department, salary))
    return employees

def save_employees(employees, filename="employees.txt"):
    with open(filename, "w") as file:
        for emp in employees:
            file.write(f"{emp.emp_id},{emp.name},{emp.designation},{emp.department},{emp.salary}\n")

def generate_employee_id(employees):
    if employees:
        return str(int(employees[-1].emp_id) + 1)
    else:
        return "1"

def get_valid_salary():
    while True:
        salary = input(f"{Fore.YELLOW}Enter Salary (must be a positive number): {Style.RESET_ALL}")
        try:
            salary = float(salary)  # The salary will convert to float
            if salary <= 0:
                print(f"{Fore.RED}Salary must be a positive number! Please try again.{Style.RESET_ALL}")
            else:
                return salary
        except ValueError:
            print(f"{Fore.RED}Invalid salary! Please enter a valid number.{Style.RESET_ALL}")

def get_non_empty_input(prompt):
    while True:
        user_input = input(f"{Fore.YELLOW}{prompt}: {Style.RESET_ALL}").strip()
        if not user_input:
            print(f"{Fore.RED}This field cannot be empty. Please provide a valid input.{Style.RESET_ALL}")
        else:
            return user_input

def add_employee(employees):
    print(f"\n{Fore.GREEN}--- Add a New Employee ---{Style.RESET_ALL}")
    emp_id = generate_employee_id(employees)
    name = get_non_empty_input("Enter Employee Name")
    designation = get_non_empty_input("Enter Employee Designation")
    department = get_non_empty_input("Enter Employee Department")
    salary = get_valid_salary()

    employee = Employee(emp_id, name, designation, department, salary)
    employees.append(employee)
    save_employees(employees)
    print(f"{Fore.GREEN}Employee added successfully!{Style.RESET_ALL}")

def update_employee(employees):
    print(f"\n{Fore.CYAN}--- Update Employee Information ---{Style.RESET_ALL}")
    search_term = input(f"{Fore.YELLOW}Enter Employee Name or Designation to update: {Style.RESET_ALL}").lower()
    for emp in employees:
        if search_term in emp.name.lower() or search_term in emp.designation.lower():
            print(f"\n{Fore.GREEN}Employee Found: {emp}{Style.RESET_ALL}")
            new_name = input(f"{Fore.YELLOW}Enter new name (Press Enter to keep current): {Style.RESET_ALL}")
            new_designation = input(f"{Fore.YELLOW}Enter new designation (Press Enter to keep current): {Style.RESET_ALL}")
            new_department = input(f"{Fore.YELLOW}Enter new department (Press Enter to keep current): {Style.RESET_ALL}")
            new_salary = input(f"{Fore.YELLOW}Enter new salary (Press Enter to keep current): {Style.RESET_ALL}")

            if new_name:
                emp.name = new_name
            if new_designation:
                emp.designation = new_designation
            if new_department:
                emp.department = new_department
            if new_salary:
                try:
                    emp.salary = float(new_salary)
                    if emp.salary <= 0:
                        print(f"{Fore.RED}Salary must be a positive number.{Style.RESET_ALL}")
                        return
                except ValueError:
                    print(f"{Fore.RED}Invalid salary input! It must be a number.{Style.RESET_ALL}")
                    return
            save_employees(employees)
            print(f"{Fore.GREEN}Employee updated successfully!{Style.RESET_ALL}")
            return
    print(f"{Fore.RED}Employee not found with that name or designation.{Style.RESET_ALL}")

def delete_employee(employees):
    print(f"\n{Fore.RED}--- Delete Employee Record ---{Style.RESET_ALL}")
    search_term = input(f"{Fore.YELLOW}Enter Employee Name or Designation to search: {Style.RESET_ALL}").lower()
    for emp in employees:
        if search_term in emp.name.lower() or search_term in emp.designation.lower():
            print(f"\n{Fore.GREEN}Employee Found: {emp}{Style.RESET_ALL}")
            confirmation = input(f"{Fore.YELLOW}Are you sure you want to delete this employee? (y/n): {Style.RESET_ALL}")
            if confirmation.lower() == 'y':
                employees.remove(emp)
                save_employees(employees)
                print(f"{Fore.GREEN}Employee deleted successfully!{Style.RESET_ALL}")
            return
    print(f"{Fore.RED}Employee not found with that name or designation.{Style.RESET_ALL}")

def view_employees(employees):
    print(f"\n{Fore.MAGENTA}--- View All Employees ---{Style.RESET_ALL}")
    if not employees:
        print(f"{Fore.RED}No employees found.{Style.RESET_ALL}")
    else:
        headers = ["ID", "Name", "Designation", "Department", "Salary"]
        table = [[emp.emp_id, emp.name, emp.designation, emp.department, emp.salary] for emp in employees]
        print(tabulate(table, headers, tablefmt="pretty"))

def search_employee(employees):
    print(f"\n{Fore.YELLOW}--- Search Employee ---{Style.RESET_ALL}")
    search_term = input(f"{Fore.YELLOW}Enter Employee Name or Designation to search: {Style.RESET_ALL}").lower()
    found = False
    headers = ["ID", "Name", "Designation", "Department", "Salary"]
    table = []
    for emp in employees:
        if search_term in emp.name.lower() or search_term in emp.designation.lower():
            table.append([emp.emp_id, emp.name, emp.designation, emp.department, emp.salary])
            found = True
    if not found:
        print(f"{Fore.RED}No employee found with that name or designation.{Style.RESET_ALL}")
    else:
        print(tabulate(table, headers, tablefmt="pretty"))

def main():
    employees = load_employees()
    
    while True:
        print(f"\n{Fore.CYAN}--- Employee Management System ---{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Add Employee{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. Update Employee{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Delete Employee{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. View All Employees{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5. Search Employee{Style.RESET_ALL}")
        print(f"{Fore.RED}6. Exit{Style.RESET_ALL}")
        
        choice = input(f"{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}")
        
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            update_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            view_employees(employees)
        elif choice == "5":
            search_employee(employees)
        elif choice == "6":
            save_employees(employees)
            print(f"{Fore.GREEN}Exiting and saving data...{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Thank you for using the Employee Management System!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    from colorama import init
    init(autoreset=True)  
    main()
