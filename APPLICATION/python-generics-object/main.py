from beans.GreetMessage import GreetMessage
from beans.WishMessage import WishMessage
from services.MessageService import MessageService

def mainExecutor()-> None:
    greetMessage: GreetMessage = GreetMessage("1","sender1","Hello, how are you?")
    wishMessage: WishMessage = WishMessage("2","sender2","Happy Birthday!")
    greetMessageService: MessageService[GreetMessage] = MessageService(greetMessage)
    wishMessageService: MessageService[WishMessage] = MessageService(wishMessage)
    print(greetMessageService.getMessage())
    print(wishMessageService.getMessage())
    
    
if __name__ == "__main__":
    mainExecutor()