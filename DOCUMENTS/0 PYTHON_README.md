# Python 
### Feb 20 1991 

## elements of python 
* scripting lang
* procedural & functional oritented 
* object oriented  
* modular programing lang.

## 30 Reserve words 
```
and			A logical operator
as			To create an alias
assert		For debugging
break		To break out of a loop
class		To define a class
continue	To continue to the next iteration of a loop
def			To define a function
del			To delete an object
elif		Used in conditional statements, same as else if
else		Used in conditional statements
except		Used with exceptions, what to do when an exception occurs
False		Boolean value, result of comparison operations
finally		Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for			To create a for loop
from		To import specific parts of a module
global		To declare a global variable
if			To make a conditional statement
import		To import a module
in			To check if a value is present in a list, tuple, etc.
is			To test if two variables are equal
lambda		To create an anonymous function
None		Represents a null value
nonlocal	To declare a non-local variable
not			A logical operator
or			A logical operator
pass		A null statement, a statement that will do nothing
raise		To raise an exception
return		To exit a function and return a value
True		Boolean value, result of comparison operations
try			To make a try...except statement
while		To create a while loop
with		Used to simplify exception handling
yield		To end a function, returns a generator
```

## Built-in Data Types
* Text Type:	str
* Numeric Types:	int, float, complex
* Sequence Types:	list, tuple, range
* Mapping Type:	dict
* Set Types:	set, frozenset
* Boolean Type:	bool
* Binary Types:	bytes, bytearray, memoryview

```
x = "Hello World"	                            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}				set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True										bool	
x = b"Hello"									bytes	
x = bytearray(5)								bytearray	
x = memoryview(bytes(5))						memoryview
```


## Arithmetic Operators
```
+	Addition	      x + y	
-	Subtraction	      x - y	
*	Multiplication    x * y	
/	Division	      x / y	
%	Modulus	          x % y	
**	Exponentiation	  x ** y	
//	Floor division	  x // y
```

## Assignment Operators
```
=		x = 5		x = 5	
+=		x += 3		x = x + 3	
-=		x -= 3		x = x - 3	
*=		x *= 3		x = x * 3	
/=		x /= 3		x = x / 3	
%=		x %= 3		x = x % 3	
//=		x //= 3		x = x // 3	
**=		x **= 3		x = x ** 3	
&=		x &= 3		x = x & 3	
|=		x |= 3		x = x | 3	
^=		x ^= 3		x = x ^ 3	
>>=		x >>= 3		x = x >> 3	
<<=		x <<= 3		x = x << 3	
```

## Comparison Operators
```
==		Equal						x == y	
!=		Not equal					x != y	
>		Greater than				x > y	
<		Less than					x < y	
>=		Greater than or equal to	x >= y	
<=		Less than or equal to		x <= y
```

## Identity Operators
```
is 			Returns True if both variables are the same object	         	x is y	
is not		Returns True if both variables are not the same object			x is not y
```

## Membership Operators
```
in 			Returns True if a sequence with the specified value is present in the object			x in y	
not in		Returns True if a sequence with the specified value is not present in the object		x not in y
```

## Bitwise Operators
```
& 		AND						Sets each bit to 1 if both bits are 1
|		OR						Sets each bit to 1 if one of two bits is 1
^		XOR						Sets each bit to 1 if only one of two bits is 1
~ 		NOT						Inverts all the bits
<<		Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>		Signed right shift		Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
```

## Built in Functions
```
abs()			Returns the absolute value of a number
all()			Returns True if all items in an iterable object are true
any()			Returns True if any item in an iterable object is true
ascii()			Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()			Returns the binary version of a number
bool()			Returns the boolean value of the specified object
bytearray()		Returns an array of bytes
bytes()			Returns a bytes object
callable()		Returns True if the specified object is callable, otherwise False
chr()			Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()		Returns the specified source as an object, ready to be executed
complex()		Returns a complex number
delattr()		Deletes the specified attribute (property or method) from the specified object
dict()			Returns a dictionary (Array)
dir()			Returns a list of the specified object's properties and methods
divmod()		Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()		Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()			Evaluates and executes an expression
exec()			Executes the specified code (or object)
filter()		Use a filter function to exclude items in an iterable object
float()			Returns a floating point number
format()		Formats a specified value
frozenset()		Returns a frozenset object
getattr()		Returns the value of the specified attribute (property or method)
globals()		Returns the current global symbol table as a dictionary
hasattr()		Returns True if the specified object has the specified attribute (property/method)
hash()			Returns the hash value of a specified object
help()			Executes the built-in help system
hex()			Converts a number into a hexadecimal value
id()			Returns the id of an object
input()			Allowing user input
int()			Returns an integer number
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()			Returns an iterator object
len()			Returns the length of an object
list()			Returns a list
locals()		Returns an updated dictionary of the current local symbol table
map()			Returns the specified iterator with the specified function applied to each item
max()			Returns the largest item in an iterable
memoryview()	Returns a memory view object
min()			Returns the smallest item in an iterable
next()			Returns the next item in an iterable
object()		Returns a new object
oct()			Converts a number into an octal
open()			Opens a file and returns a file object
ord()			Convert an integer representing the Unicode of the specified character
pow()			Returns the value of x to the power of y
print()			Prints to the standard output device
property()		Gets, sets, deletes a property
range()			Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()			Returns a readable version of an object
reversed()		Returns a reversed iterator
round()			Rounds a numbers
set()			Returns a new set object
setattr()		Sets an attribute (property/method) of an object
slice()			Returns a slice object
sorted()		Returns a sorted list
@staticmethod()	Converts a method into a static method
str()			Returns a string object
sum()			Sums the items of an iterator
super()			Returns an object that represents the parent class
tuple()			Returns a tuple
type()			Returns the type of an object
vars()			Returns the __dict__ property of an object
zip()			Returns an iterator, from two or more iterators
```