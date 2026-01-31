class Wish :
    
    def __init__(self, description:str):
        self.description = description;
        
    
    def make_wish(self) -> str:
        return f"Wish made: {self.description}"
           