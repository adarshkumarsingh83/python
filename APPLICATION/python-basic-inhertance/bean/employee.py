from bean.person import Person


class Employee(Person):
    message = "Employee Message"
    employeeId = 0
    deptName = ''

    # Constructor() of the Employee
    def __init__(self, employeeId=0, deptName=''):
        print("Employee Constructor")
        self.employeeId = employeeId
        self.deptName = deptName

    # Constructor() of the Employee
    def __init__(self, employeeId=0, deptName='', personId=0, firstName='xxx', lastName='xxx'):
        print("Employee Constructor")
        super(Employee, self).__init__(personId, firstName, lastName)
        self.employeeId = employeeId
        self.deptName = deptName

    # display() of the Employee
    def display(self):
        super(Employee,self).display();
        print("Employeeid " + str(self.employeeId) + " DeptName " + self.deptName)

    # distructor() of the Employee
    def __del__(self):
        print("Employee Destructor")
