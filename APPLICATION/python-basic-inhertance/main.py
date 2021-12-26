from bean.person import Person
from bean.employee import Employee


def main_function_executor():
    # Object creeation of the person
    personObject = Person(100, 'adarsh', 'kumar')
    # invoking the display() of the person
    personObject.display()

    # Object creation of the Employee
    employeeObject = Employee(1111, 'IT')
    employeeObject.display()
    print(employeeObject.message)

    # Object creation of the Employee
    employeeObject = Employee(1111, 'IT', 100, 'adarsh', 'kumar')
    employeeObject.display()
    print(employeeObject.message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_function_executor()
