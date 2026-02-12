from __future__ import annotations

class DataProcessor[T]:
    
    def __init__(self):
        pass
    
    def processData(self, dataItem: [T])-> list[T]:
        # Placeholder for data processing logic
        for item in dataItem:
            print(f"Processed item: {item}")
        return dataItem[::-1]