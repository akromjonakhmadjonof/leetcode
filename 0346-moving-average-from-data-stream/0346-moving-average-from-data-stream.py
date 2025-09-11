import collections
class MovingAverage:
    def __init__(self, size: int):
        self.size = size # Stores the size of sliding window
        self.queue = collections.deque() # Stores the elements in queue
        

    def next(self, val: int) -> float:

        if len(self.queue) ==  self.size:
            self.queue.popleft() # Pop from left if the length of the queue exceeds the size
        # Returning the average of sliding window 
        
        self.queue.append(val)

        return sum(self.queue) / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)