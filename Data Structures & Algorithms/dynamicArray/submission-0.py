class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0]*capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        # temp = capacity[i]
        # capacity[i] = capacity[n]
        # capacity[n] = temp



    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1 

        # capacity.append(n)


    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]
    def resize(self) -> None:
        new_arr = [0] * (self.capacity * 2)
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
        # return len(self.capacity.size)-1
        
    
    def getCapacity(self) -> int:
        return self.capacity

