class Message:
    
    def __init__(self, content:str, sender:str,receiver :str):
        self.content = content
        self.author = sender
        self.receiver  = receiver 

    def display(self):
        return f"{self.author}: {self.content} : {self.receiver }"