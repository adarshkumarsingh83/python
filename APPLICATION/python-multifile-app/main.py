from espark_io.user_input import InputClass

try:
    inputClass = InputClass()
    name = inputClass.get_input()
    print("Input Value from User is => "+name)

except Exception:
    print("Some things went wrong ")
