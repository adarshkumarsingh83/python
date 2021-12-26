
from bean.person import Person

def main_function_executor():
    personObject = Person()
    # calling the setter() of the person
    personObject.setName(101, "adarsh", "kumar")
    # invoking the display() of the person
    personObject.display()

    personObject = Person()
    personObject.display()

if __name__ == '__main__':
    main_function_executor()
