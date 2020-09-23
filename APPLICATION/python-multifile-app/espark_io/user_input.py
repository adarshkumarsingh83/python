
class InputClass:

    def __init__(self):
        print("InputClass Constructor")


    def get_input(self):
        try:
            return raw_input("enter your name ")
        except NameError:
            print "Not a valid Name"
        except ValueError:
            print("Not a Valid Value")