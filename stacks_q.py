class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push the new element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, pop all elements from stack1 and push them onto stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty, so we can raise an exception or return a specific value
        if not self.stack2:
            raise IndexError("dequeue from an empty queue")
        
        # The top element of stack2 is the front of the queue
        return self.stack2.pop()

queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.dequeue())  
queue.enqueue(4)
print(queue.dequeue()) 
print(queue.dequeue()) 
