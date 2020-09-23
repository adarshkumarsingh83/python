
class EsparkWorld:

    def __init__(self):
        print("EsparkWorld Constructor")

    def helloworld(self,out):
        out.write("Hello world of Python\n")


    def esparkworld(self):
        return "welcome from espark in world of Python\n"


esparkWorld = EsparkWorld()
print(esparkWorld.esparkworld())
