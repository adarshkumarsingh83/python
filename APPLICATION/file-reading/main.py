import sys 
from typing import Generator

def readFile(path: str) -> Generator[str, None, str]:
    """Reads a file line by line."""
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()
            

def main() -> None:
    reader : Generator[str, None, str] = readFile('data.txt')
    input('Press Enter to start reading the file...')
    while True:
        try:
            line = next(reader)
            print(line)
        except StopIteration as e:
            print('End of file reached.',e.value)
            sys.exit(0)
        input('Press Enter to read the next line...')
        
if __name__ == '__main__':
    main()