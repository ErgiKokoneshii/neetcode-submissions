class DynamicArray:
    def __init__(self, capacity: int):
        self.data = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        self.data[self.size] = n
        self.size += 1
    
    def popback(self) -> int:
        val = self.data[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        self.capacity *= 2
        new_data = [0] * self.capacity
        for i in range(len(self.data)):
            new_data[i] = self.data[i]
        self.data = new_data
    
    def getSize(self) -> int:
        return self.size    
    
    def getCapacity(self) -> int:
        return self.capacity