from PythonLab3.queue.queue_interface import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.array = []
        self.front = 0
        self.rear = -1
        self.MAX_SIZE = 5

    def enqueue(self, element):
        if self.is_full():
            print(f"Queue is full. Cannot enqueue element: {element}")
            return
        self.rear = (self.rear + 1) % self.MAX_SIZE
        self.array[self.rear] = element

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
            return None
        dequeued = self.array[self.front]
        self.front = (self.front + 1) % self.MAX_SIZE
        return dequeued

    def peek(self):
        if self.is_empty():
            print("Queue is empty. No element to peek.")
            return None
        return self.array[self.front]

    def is_empty(self):
        return (self.rear + 1 - self.front) % self.MAX_SIZE == 0

    def is_full(self):
        return (self.rear + 2 - self.front) % self.MAX_SIZE == 0


class ArrayDownQueue(Queue):
    def __init__(self):
        self.array = [None] * 5
        self.front = 0
        self.rear = 0
        self.MAX_SIZE = 5

    def enqueue(self, element):
        if self.is_full():
            print(f"Queue is full. Cannot enqueue element: {element}")
            return
        self.array[self.front] = element
        self.front = (self.front - 1) % self.MAX_SIZE

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
            return None
        dequeued = self.array[self.rear]
        self.array[self.rear] = None
        self.rear = (self.rear - 1) % self.MAX_SIZE
        return dequeued

    def peek(self):
        if self.is_empty():
            print("Queue is empty. No element to peek.")
            return None
        return self.array[self.rear]

    def is_empty(self):
        return self.front == self.rear and self.array[self.rear] is None

    def is_full(self):
        return (self.front - 1) % self.MAX_SIZE == self.rear and self.array[self.rear] is not None
