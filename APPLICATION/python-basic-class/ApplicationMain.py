from bean.Message import Message

class ApplicationMain:
    
    def generate_message(message:str, sender:str, receiver:str) -> Message:
        return Message(me, sender, receiver)

    def displayMessage(msg:Message):
        print(msg.display())
        
    def main(self):
        msg = self.generate_message("Hello, how are you?", "Adarsh", "Radha")
        self.displayMessage(msg)
        
        
def driverMain():
    app = ApplicationMain()
    app.main()
            

if __name__ == '__main__':
    driverMain()