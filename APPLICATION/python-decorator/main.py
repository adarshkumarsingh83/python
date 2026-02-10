from service.GreetService import GreetService

def main():
    greet_service = GreetService()
    greeting_message: str = greet_service.greet('adarsh')
    print(greeting_message)
    
if __name__ == "__main__":
    main()