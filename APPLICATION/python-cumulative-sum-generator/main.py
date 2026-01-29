from typing import Generator

def generate_numbers() -> Generator[float, float, None]:
    total :float  = 0.0
    while True:
        increment :float  = yield total
        total += increment
        
def main() -> None:
    gen :Generator[float, float, None]  = generate_numbers()
    next(gen)  # Prime the generator
    
    while True:
        try:
            user_input :str  = input("Enter a number to add (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            number :float  = float(user_input)
            current_total :float  = gen.send(number)
            print(f"Current total: {current_total}")
        except ValueError:
            print("Please enter a valid number.")
    
if __name__ == '__main__':
    main()
    