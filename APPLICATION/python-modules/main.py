from utils.GreetModule import Greet 
from utils.WishModule import Wish

def main():
    greeter = Greet("Adarsh kumar")
    print(greeter.say_hello())
    
    wisher = Wish("I wish for a new bike")
    print(wisher.make_wish())
    
    
if __name__ == "__main__":
    main()