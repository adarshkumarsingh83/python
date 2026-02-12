from __future__ import annotations

class MessageService[T]:
  
    def __init__(self, message: T):
        self.message = message

    def getMessage(self) -> T:
        return f"Message: {self.message.__str__()}"