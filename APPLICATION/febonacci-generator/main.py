from typing import Generator

def generate_numbers() -> Generator[int, None, None]:
    a,b  = 0, 1
    while True:
        yield a
        a, b = b, ( a + b )
       
def main() -> None:
    febonacci_gen: Generator[int, None, None] = generate_numbers()
    n: int = 10;
    line_break = str = '_' *20
    while True: 
        input(f'Press Enter to get next {n} Fibonacci numbers ')
        print(line_break)
        for i in range(n):
            print(f'{next(febonacci_gen)}')
            
        print(line_break)
    
if __name__ == "__main__":
    main()