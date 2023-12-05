from PythonLab3.stack.stack_interface import Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack(Stack):
    def __init__(self):
        self.top = None
        self.size = 0
        self.MAX_SIZE = 5

    def push(self, element):
        if self.is_full():
            print(f"Stack is full. Cannot push element: {element}")
            return
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop element.")
            return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped

    def element(self):
        if self.is_empty():
            print("Stack is empty. No element to peek.")
            return None
        return self.top.data

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.MAX_SIZE
