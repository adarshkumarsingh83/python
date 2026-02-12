class GreetMessage:
  
    def __init__(self,id:str,senderId:str,content:str):
        self.id = id
        self.senderId = senderId
        self.content = content
        
    def get_message(self)-> str:
        return self.content
    
    def __str__(self):
        return f"GreetMessage(id={self.id}, senderId={self.senderId}, content={self.content})"