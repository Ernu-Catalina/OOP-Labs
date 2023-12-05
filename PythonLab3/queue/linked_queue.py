from PythonLab3.queue.queue_interface import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue(Queue):
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.MAX_SIZE = 5

    def enqueue(self, element):
        if self.is_full():
            print(f"Queue is full. Cannot enqueue element: {element}")
            return
        new_node = Node(element)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element.")
            return None
        dequeued = self.front.data
        self.front = self.front.next
        self.size -= 1
        return dequeued

    def peek(self):
        if self.is_empty():
            print("Queue is empty. No element to peek.")
            return None
        return self.front.data

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.MAX_SIZE