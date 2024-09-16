from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees(employees):
    if not employees:
        print("No employees found.")
    for employee in employee:
        print(employee)

def find_employee_by_name(employees, name):
    for employee in employees:
        if employee.name.lower() == name.lower():
            return employee
    return "Employee not found."


def find_employee_by_id(emp_id, employees):
    for employee in employees:
        if employee.emp_id == emp_id:
            return employee
    return "Employee not found."


def create_employee(emp_id, name, department, employees):
    if find_employee_by_id(emp_id) == "Employee not found.":
        new_employee = Employee(emp_id, name, department)
        employees.append(new_employee)
        print(f"Employee {name} created successfully.")
    else:
        print("An employee with this ID already exists.")


def update_employee(emp_id, name=None, department=None):
    employee = find_employee_by_id(emp_id)
    if isinstance(employee, Employee):
        if name:
            employee.name = name
        if department:
            employee.department = department
        print(f"Employee {emp_id} update successfully.")
    else:
        print(employee)


def delete_employee(emp_id, employees):
    employee = find_employee_by_id(emp_id)
    if isinstance(employee, Employee):
        employees.remove(employee)
        print(f"Employee {emp_id} deleted successfully.")
    else:
        print(employee)


def list_department_employees(department, employees):
    dept_employees = [emp for emp in employees if emp.department.lower() == department.lower()]
    if dept_employees:
        for emp in dept_employees:
            print(emp)
    else:
        print(f"No employees found in the {department} department.")