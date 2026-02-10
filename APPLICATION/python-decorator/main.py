from service.GreetService import GreetService

def main():
    greet_service = GreetService()
    name = input("Enter name (press Enter for default 'adarsh'): ").strip()
    if not name:
        name = 'adarsh'
    greeting_message: str = greet_service.greet(name)
    print(greeting_message)
    
if __name__ == "__main__":
    main()