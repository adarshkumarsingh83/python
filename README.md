# python
python concept pos samples 



>>> 10+20
30
>>> 59-3
56
>>> var = 1000
>>> var
1000
>>> var+100
1100
>>> var -333
667
>>> var =var -333
>>> var
667
>>> var
667
>>> var = var+333
>>> var
1000

##Taking input from console 
>>> var = input("Enter the Name")
Enter the NameADarsh kumar 
>>> var
'ADarsh kumar '

##Taking input and converting into the int type 
>>> var = int(input("Enter the Number "))
Enter the Number 30
>>> var + 40
70
>>> var
30

## Taking input from console which is string by default ##################################################################################
>>> var = input("Enter the Value") 
>>> var  //printing the value of the var variable 

## Taking input from console and type casted into the int ##################################################################################
>>> var =int(input("Enter the Value")) 
>>> var  //printing the value of the var variable 
>>> var + 50 // this will work becoz both are int value 

##To get the list of all the built in function of the python ##################################################################################
>>> dir(__builtins__) 

##to get the help for the mentioned function of the python##################################################################################
>>> help(<name of the function>) 
eg 
>>> help(max) //return the help related to the max function ##################################################################################

##To import the build in module of python
>>> import math
>>> math.factorial
<built-in function factorial>
>>> math.factorial(5)
120

##Storing function into the variable##################################################################################
>>> factorial = math.factorial
>>> factorial(5)
120

##python script development and execution ##################################################################################

python gui -> file -> new file -> save as <name of the file>
NOTE: new window will be open to type the code for the file 
----------------------------------------------------------
sum.py
----------------------------------------------------------

# Input value 1 and type casted it from string to int 
value1=int(input("Enter the number"))

# Input value 2 and type casted it from string to int 
value2=int(input("Enter the number"))

# adding both input and then type casted to string and concatinated with string msg 
print("Sum of the Values are :=> "+ str(value1+value2))

#to w8 until the use wants 
input("Press Enter to Exit ....")
----------------------------------------------------------
# To execute the code 
Code Window -> Run -> Run Module 
>>> ========================================== RESTART ==========================================
>>> 
Enter the number10
Enter the number20
Sum of the Values are :=> 30
>>> 


##String in python can be enclosed with single quotes or double quotes or triple quotes its only string 
>>> stringVar='adarsh'
>>> stringVar
'adarsh'

>>> stringVar="adarsh"
>>> stringVar
'adarsh'

stringVar="""adarsh"""
>>> stringVar
'adarsh'

## Plus + is the concatination operator in string 
>>> varString1="adarsh"
>>> varString2="kumar"
>>> print(varString1+varString2)
adarshkumar

##Printing same string multiple times 
>>> var = "espark "
>>> print( var * 5)
espark espark espark espark espark

##List Type in python ##################################################################################
# it can hold hetrogenious data types value
#empty list is the valid  in python
>>> names=[]
>>> names
[]

#To add the value 
>>> names.append("sonu")
>>> names
['sonu']

#To add the value to specific index 
>>> names.insert(1,"adarsh")
>>> names
['adarsh']


#non empty list with postive and negative index number
>>> names=["adarsh","radha","amit"]
>>> names
['adarsh', 'radha', 'amit']
>>> names[0]
'adarsh'
>>> names[1]
'radha'
>>> names[2]
'amit'
>>> names[-1]
'amit'
>>> names[-2]
'radha'
>>> names[-3]
'adarsh'
>>> names.append("sonu")
>>> names
['adarsh', 'radha', 'amit', 'sonu']

##merging hetrogenious datatype lists 
>>> names=["adarsh","radha"]
>>> names
['adarsh', 'radha']

>>> phone=[123456789,987654321]
>>> phone
[123456789,987654321]

>>> print(names,phone)
['adarsh', 'radha'] [123456789, 987654321]

>>> names.extend(phone)
>>> names
['adarsh', 'radha', 123456789, 987654321]

##Slicing the list 
>>> intList=[1,2,3,4,5,6,7,8,9]
>>> intList
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> intList[2:7]   //list[startValue:endValue]
[3, 4, 5, 6, 7]
>>> intList[2: ]   //list[startValue:end]
[3, 4, 5, 6, 7, 8, 9]
>>> intList[ :7]   //list[start:endValue]
[1, 2, 3, 4, 5, 6, 7]
>>> intList[:] //list[start:end]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> intList

>>> intList=[0,1,2,3,4,5,6,7,8,9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> intList[0:9:3] //intList[startValue:endValue:every X Value in List Till End]
[0, 3, 6]
>>> intList[0:9:2]
[0, 2, 4, 6, 8]
>>> intList[0:9:4]
[0, 4, 8]
>>> 

#Looping into the list 
>>> for i, v in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(i, v)
    
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9

##Function in List
--------------------
min(list)	Returns the minimum value from the list given.
max(list)	Returns the largest value from the given list.
len(list)	Returns number of elements in a list.
cmp(list1,list2)	Compares the two list.
list(sequence)	Takes sequence types and converts them to lists.
index(object)	Returns the index value of the object.
count(object)	It returns the number of times an object is repeated in list.
pop()/pop(index)	Returns the last object or the specified indexed object. It removes the popped object.
insert(index,object)	Insert an object at the given index.
extend(sequence)	It adds the sequence to existing list.
remove(object)	It removes the object from the given List.
reverse()	Reverse the position of all the elements of a list.
sort()	It is used to sort the elements of the List.


##Python Tuple##################################################################################
A tuple is a sequence of immutable objects, therefore tuple cannot be changed.
>>> tupleObject=()
>>> tupleObject
()

>>> tupleObject1=(10,20,30);
>>> tupleObject1
(10, 20, 30)
>>> tupleObject2=(40,50,60); 
>>> tupleObject2
(40, 50, 60)
>>> tupleObject1+tupleObject2
(10, 20, 30, 40, 50, 60)

##Functions
-----------------
min(tuple)	Returns the minimum value from a tuple.
max(tuple)	Returns the maximum value from the tuple.
len(tuple)	Gives the length of a tuple
cmp(tuple1,tuple2)	Compares the two Tuples.
tuple(sequence)	Converts the sequence into tuple.

##Sets Type in python  ##################################################################################
>>> fruitsBasket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> fruitsBasket
{'apple', 'orange', 'banana', 'pear'}

>>> for fruit in sorted(fruitsBasket):
   print(fruit)
   
apple
banana
orange
pear

>>> characterSet = set('adarshkumar')
>>> characterSet
{'r', 's', 'd', 'a', 'k', 'u', 'h', 'm'}

##Dictionaries ##################################################################################
>>> employee = {'name': 'adarsh', 'phone': 987654321}
>>> employee
{'phone': 987654321, 'name': 'adarsh'}

>>> employee=dict([('name', 'adarsh'), ('phone', 987654321)])
>>> employee
{'phone': 987654321, 'name': 'adarsh'}

#Looping in dictionary
>>> for k, v in employee.items():
     print(k, v)
	      
phone 987654321
name adarsh

##Functions
------------
len(dictionary)	Gives number of items in a dictionary.
cmp(dictionary1,dictionary2)	Compares the two dictionaries.
str(dictionary)	Gives the string representation of a string.
keys()	Return all the keys element of a dictionary.
values()	Return all the values element of a dictionary.
items()	Return all the items(key-value pair) of a dictionary.
update(dictionary2)	It is used to add items of dictionary2 to first dictionary.
clear()	It is used to remove all items of a dictionary. It returns an empty dictionary.
fromkeys(sequence,value1)/ fromkeys(sequence)	It is used to create a new dictionary from the sequence where sequence elements forms the key and all keys share the values ?value1?. In case value1 is not give, it set the values of keys to be none.
copy()	It returns an ordered copy of the data.
has_key(key)	It returns a boolean value. True in case if key is present in the dictionary ,else false.
get(key)	Returns the value of the given key. If key is not present it returns none.

##Dque in python ##################################################################################
>>> from collections import deque
>>> queue = deque(["adarsh", "radha", "amit"])
>>> queue.append("sonu")
>>> queue.append("monu")
>>> queue
deque(['adarsh', 'radha', 'amit', 'sonu', 'monu'])
>>> queue.popleft()
'adarsh'
>>> queue.popleft()
'radha'
>>> queue.popleft()
'amit'
>>> queue.popleft()
'sonu'
>>> queue.popleft()
'monu'

## Stacks in python##################################################################################
>>> stack = []
>>> stack.append("adarsh")
>>> stack.append("radha")
>>> stack.append("amit")
>>> stack.pop()
'amit'
>>> stack.pop()
'radha'
>>> stack.pop()
'adarsh'
>>> 



##if else condition in python ##################################################################################
python gui -> file -> new file -> save as <name of the file>
NOTE: new window will be open to type the code for the file 
----------------------------------------------------------
sum.py
----------------------------------------------------------

# Input value 1 and type casted it from string to int 
value1=int(input("Enter the number with in 10 "))

# Input value 2 and type casted it from string to int 
value2=int(input("Enter the number with in 10 "))

#if condition to validate the input values 
if (value1>0) and (value2>10):
    print("Enter Values is Not Valid its out of Range of 10 ")
else :
   print("Sum of the Values are :=> "+ str(value1+value2))

#to w8 until the use wants 
input("Press Enter to Exit ....")
----------------------------------------------------------
# To execute the code 
Code Window -> Run -> Run Module 

>>> ========================================== RESTART ==========================================
>>> 
Enter the number with in 10 5
Enter the number with in 10 89
Enter Values is Not Valid its out of Range of 10 
Press Enter to Exit ....


##Elseif 

if   <condition> :
		<statements.........>
elif <condition>:
		<statements.........>
elif <condition>:
		<statements.........>
else:
	    <statements.........>		

##Nested if else 
if   <condition> :     
		if   <condition> :     
				<statements.........>
		else:
	            <statements.........>	
else:
	    <statements.........>		


##Loops in python ##################################################################################
#while loop 
>>> index=0
>>> while(index<5):
	print(index)
	index+=1
0
1
2
3
4		

python gui -> file -> new file -> save as <name of the file>
NOTE: new window will be open to type the code for the file 
----------------------------------------------------------
sum.py
----------------------------------------------------------
execution = 'Y'
while(execution == 'Y' or execution == 'y') : 
    
        value1=int(input("Enter the number with in 10 "))
        value2=int(input("Enter the number with in 10 "))

        if (value1>0) and (value2>10):
            print("Enter Values is Not Valid its out of Range of 10 ")
        else :    
            print("Sum of the Values are :=> "+ str(value1+value2))

        execution = input("Do You Want to Continue Type Y|y or for Exit N|n")
----------------------------------------------------------
# To execute the code 
Code Window -> Run -> Run Module 

#For each Loop in python
>>> intList=[1,2,3,4,5]
>>> for elementInList in intList :
	print(elementInList)	
1
2
3
4
5


##Custom Function and its Call  ##################################################################################
#Function with no return value 
>>> def wish(name):
	print("Welcome to the Espark ",name)
	
>>> wish("Adarsh")
Welcome to the Espark  Adarsh
		
#Function with return value 		
>>> wish("Adarsh")
Welcome to the Espark  Adarsh
>>> def wish(name):
	return "welcome to the Espark "+str(name)

>>> print(wish("adarsh"))
welcome to the Espark adarsh

#Function with default values 
>>> def wish (name="unknown",age=0):
	print(name,age)

>>> wish()
unknown 0
>>> wish("adarsh")
adarsh 0
>>> wish("adarsh",30)
adarsh 30
>>>  		

#Function with multivalued parameter  ##################################################################################
>>> def studentData(name,*marks):
	print(name)
	print(marks)

>>> studentData("adarsh");
adarsh
()
>>> studentData("adarsh",10)
adarsh
(10,)
>>> studentData("adarsh",10,20)
adarsh
(10, 20)
>>> studentData("adarsh",50,60,70)
adarsh
(50, 60, 70)


##Custom Modules in python ##################################################################################

python gui -> file -> new file -> save as <name of the file>
NOTE: new window will be open to type the code for the file 
----------------------------------------------------------
summodule.py
----------------------------------------------------------
def sum1(): 
	execution = 'Y'
	while(execution == 'Y' or execution == 'y') : 
		
			value1=int(input("Enter the number with in 10 "))
			value2=int(input("Enter the number with in 10 "))

			if (value1>0) and (value2>10):
				print("Enter Values is Not Valid its out of Range of 10 ")
			else :    
				print("Sum of the Values are :=> "+ str(value1+value2))

			execution = input("Do You Want to Continue Type Y|y or for Exit N|n")
			
		

def sum2(value1,value2): 				

			if (value1>0) and (value2>10):
				print("Enter Values is Not Valid its out of Range of 10 ")
			else :    
				print("Sum of the Values are :=> "+ str(value1+value2))

			input("Press Enter to Exit")		
			
----------------------------------------------------------			
			
>>> import sys
>>> sys.path.insert(0,"C:\\Users\\adarsh_k\\Desktop")
>>> import summodule
>>> summodule.sum1()
Enter the number with in 10 3
Enter the number with in 10 4
Sum of the Values are :=> 7
Do You Want to Continue Type Y|y or for Exit N|ny
Enter the number with in 10 2
Enter the number with in 10 5
Sum of the Values are :=> 7
Do You Want to Continue Type Y|y or for Exit N|nn
>>> summodule.sum2(5,7)
Sum of the Values are :=> 12
Press Enter to Exit

##Classes and object in python  ##################################################################################

NOTE:Every member function required self as a argument 
-------------------------------------------------------------
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

#Object creeation of the person 
personObject=Person()
#calling the setter() of the person 
personObject.setName(101,"adarsh","kumar")
#invoking the display() of the person 
personObject.display()       
>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
Person Id: 101 FirstName: adarsh LastName: kumar
>>> 
        
-------------------------------------------------------------
##Constructor Overloading with default parameter in python  ##################################################################################
-------------------------------------------------------------
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
>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
Person Id: 100 FirstName: adarsh LastName: kumar
Person Constructor
Person Destructor
Person Id: 101 FirstName: radha LastName: singh
>>> 
		
		
---------------------------------------------------------------------------------------------------------
##Inhertance in python  ##################################################################################
---------------------------------------------------------------------------------------------------------
#Empty implemenation of the child class 
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
>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
Person Id: 100 FirstName: adarsh LastName: kumar
Person Constructor
Person Id: 0 FirstName:  LastName: 
>>> 

---------------------------------------------------------------------------------------------------
#Non Empty implementation of the child class ##################################################################################
---------------------------------------------------------------------------------------------------

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

>>> ========================================== RESTART ==========================================
>>> 
Person Constructor
Person Id: 100 FirstName: adarsh LastName: kumar
Person Message
Employee Constructor
Employeeid 1111 DeptName IT
Employee Message


-------------------------------------------------------------------------------------------------
#Multiple class inhertance in pyton ##################################################################################
-------------------------------------------------------------------------------------------------

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


------------------------------------------------------------------------------------------------------
Exception Handling in Python ##################################################################################
------------------------------------------------------------------------------------------------------
Exception hierarchy
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
		   
		   
		   
try:

     <risky code >

except Exception as e	
   print("Unexpected error:", sys.exc_info()[0])
except:
    print("Unexpected error:", sys.exc_info()[0])      
finally:
	print("executing finally clause")	
	
		
--------------------------------------------------------------------------
Custom Excpetion 	##################################################################################
--------------------------------------------------------------------------	
class AppilcatonException (Exception):
    """Base class for exceptions in this module."""
    pass

try:
     
	 if <condition> :
	      raise AppilcatonException
	 else:
          <some code> 
except AppilcatonException as e	
   print("AppilcatonException :", sys.exc_info()[0])
except:
    print("Unexpected error:", sys.exc_info()[0])      
finally:
	print("executing finally clause")	
	

