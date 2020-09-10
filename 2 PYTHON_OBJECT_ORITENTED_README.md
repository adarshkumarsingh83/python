# Classes and object in python  

* NOTE:Every member function required self as a argument 
```
class Person:

    #constructor of the person 
    def __init__(self):
        print("Person Constructor")

    #setter() of the person 
    def setName(self ,personId, firstName , lastName):
        self.personId=personId
        self.firstName=firstName
        self.lastName=lastName

    #getter() of the person class 
    def getName(self):
        return self.firstname+" "+self.lastName+" "+str(self.personId)

    #display() of the person class
    def display(self):
        print("Person Id: "+str(self.personId)+" FirstName: "+self.firstName+" LastName: "+self.lastName)

    #distructor() of the person
    def __del__(self):
        print("Person Destructor")

* Object creeation of the person 
personObject=Person()
#calling the setter() of the person 
personObject.setName(101,"adarsh","kumar")
#invoking the display() of the person 
personObject.display()       
```
* Execution of the class 
```
>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
Person Id: 101 FirstName: adarsh LastName: kumar
>>> 
```

---

# Constructor Overloading with default parameter in python  
```
class Person:

    #constructor of the person    
    def __init__(self, personId = 0, firstName ="", lastName=""):
        print("Person Constructor")
        self.personId=personId
        self.firstName=firstName
        self.lastName=lastName
        

    #setter() of the person 
    def setName(self ,personId, firstName , lastName):
        self.personId=personId
        self.firstName=firstName
        self.lastName=lastName

    #getter() of the person class 
    def getName(self):
        return self.firstname+" "+self.lastName+" "+str(self.personId)

    #display() of the person class
    def display(self):
        print("Person Id: "+str(self.personId)+" FirstName: "+self.firstName+" LastName: "+self.lastName)

    #distructor() of the person
    def __del__(self):
        print("Person Destructor")

#Object creeation of the person 
personObject=Person()
#calling the setter() of the person 
personObject.setName(100,"adarsh","kumar")
#invoking the display() of the person 
personObject.display()

#Object creeation of the person 
personObject=Person(101,"radha","singh")
#invoking the display() of the person 
```

* Exceuction of code 
```
>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
Person Id: 100 FirstName: adarsh LastName: kumar
Person Constructor
Person Destructor
Person Id: 101 FirstName: radha LastName: singh
>>> 

```

---

# Inhertance in python  

## Empty implemenation of the child class 
```
class Person:

    message="Person Class Message"
     
    #constructor of the person    
    def __init__(self, personId = 0, firstName ="", lastName=""):
        print("Person Constructor")
        self.personId=personId
        self.firstName=firstName
        self.lastName=lastName
        
    #setter() of the person 
    def setName(self ,personId, firstName , lastName):
        self.personId=personId
        self.firstName=firstName
        self.lastName=lastName

    #getter() of the person class 
    def getName(self):
        return self.firstname+" "+self.lastName+" "+str(self.personId)

    #display() of the person class
    def display(self):
        print("Person Id: "+str(self.personId)+" FirstName: "+self.firstName+" LastName: "+self.lastName)

    #distructor() of the person
    def __del__(self):
        print("Person Destructor")

class Employee (Person):
    #for not implementing the child we have to use pass k/w
    pass

#Object creeation of the person 
personObject=Person()
#calling the setter() of the person 
personObject.setName(100,"adarsh","kumar")
#invoking the display() of the person 
personObject.display()


#Object creation of the Employee
employeeObject=Employee()
employeeObject.display()
```
* Execution of the class 
```
>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
Person Id: 100 FirstName: adarsh LastName: kumar
Person Constructor
Person Id: 0 FirstName:  LastName: 
>>> 
```

## Non Empty implementation of the child class 
```

class Person:

    message="Person Message"
     
    #constructor of the person    
    def __init__(self, personId = 0, firstName ="", lastName=""):
        print("Person Constructor")
        self.personId=personId
        self.firstName=firstName
        self.lastName=lastName
        
    #display() of the person class
    def display(self):
        print("Person Id: "+str(self.personId)+" FirstName: "+self.firstName+" LastName: "+self.lastName)

    #distructor() of the person
    def __del__(self):
        print("Person Destructor")

class Employee (Person):

    message="Employee Message"
    
    #Constructor() of the Employee    
    def __init__(self, employeeId=0, deptName=""):
        print("Employee Constructor")
        self.employeeId=employeeId
        self.deptName=deptName
        
    #display() of the Employee
    def display(self):
        print("Employeeid "+str(self.employeeId)+" DeptName "+self.deptName)

    #distructor() of the Employee
    def __del__(self):
         print("Employee Destructor")
              


#Object creeation of the person 
personObject=Person(100,"adarsh","kumar")
#invoking the display() of the person 
personObject.display()
print(personObject.message)

#Object creation of the Employee
employeeObject=Employee(1111,"IT")
employeeObject.display()
print(employeeObject.message)
```
* Class Execution 
```
>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
Person Id: 100 FirstName: adarsh LastName: kumar
Person Message
Employee Constructor
Employeeid 1111 DeptName IT
Employee Message
```

## Multiple class inhertance in pyton 
```
class Father:

    messageFather="Father Message"
     
    #constructor of the Father    
    def __init__(self, firstName ="", lastName=""):
        print("Person Constructor")      
        self.firstName=firstName
        self.lastName=lastName
        
    #display() of the Father class
    def display(self):
        print("FirstName: "+self.firstName+" LastName: "+self.lastName)

    #distructor() of the Father
    def __del__(self):
        print("Father Destructor")


class Mother:

    messageMother="Mother Message"
     
    #constructor of the Father    
    def __init__(self, firstName ="", lastName=""):
        print("Mother Constructor")       
        self.firstName=firstName
        self.lastName=lastName
        
    #display() of the Mother class
    def display(self):
        print("FirstName: "+self.firstName+" LastName: "+self.lastName)

    #distructor() of the Mother
    def __del__(self):
        print("Mother Destructor")
        

class Child (Father,Mother):

    messageChild="Child Message"
    
    #Constructor() of the Child    
    def __init__(self, firstName ="", lastName=""):
        print("Child Constructor")       
        self.firstName=firstName
        self.lastName=lastName
        
    #display() of the Child
    def display(self):
        print("FirstName: "+self.firstName+" LastName: "+self.lastName)

    #distructor() of the Child
    def __del__(self):
         print("Child Destructor")
              

#Father Operations
fatherObject=Father("Niranjan","Singh")
fatherObject.display();
print(fatherObject.messageFather)

#Mother Operation
motherObject=Mother("Usha","Singh")
motherObject.display();
print(motherObject.messageMother)


#Child Operation
childObject=Child("adarsh","kumar")
childObject.display();
print(childObject.messageChild)
print(childObject.messageFather)
print(childObject.messageMother)
```
* Exeucution 
```
>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
FirstName: Niranjan LastName: Singh
Father Message
Mother Constructor
FirstName: Usha LastName: Singh
Mother Message
Child Constructor
FirstName: adarsh LastName: kumar
Child Message
Father Message
Mother Message
```

---

