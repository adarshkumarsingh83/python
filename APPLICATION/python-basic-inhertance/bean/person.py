class Person(object):

    # constructor of the person
    def __init__(self):
        print("Person Default Constructor")

    def __init__(self, personId=0, firstName='xxx', lastName='xxx'):
        self.personId = personId
        self.firstName = firstName
        self.lastName = lastName
        print("Person Parameterized Constructor")

    # setter() of the person
    def setName(self, personId=0, firstName='xxx', lastName='xxx'):
        self.personId = personId
        self.firstName = firstName
        self.lastName = lastName

    # getter() of the person class
    def getName(self):
        return self.firstname + " " + self.lastName + " " + str(self.personId)

    # display() of the person class
    def display(self):
        print("Person Id: " + str(self.personId) + " FirstName: " + self.firstName + " LastName: " + self.lastName)

    # distructor() of the person
    def __del__(self):
        print("Person Destructor")