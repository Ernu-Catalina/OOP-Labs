from PythonLab3.stack.stack_interface import Stack


class ArrayUpStack(Stack):
    def __init__(self):
        self.array = []
        self.top = -1
        self.MAX_SIZE = 5

    def push(self, element):
        if self.is_full():
            print(f"Stack is full. Cannot push element: {element}")
            return
        self.top += 1
        self.array.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop element.")
            return None
        popped = self.array.pop()
        self.top -= 1
        return popped

    def element(self):
        if self.is_empty():
            print("Stack is empty. No element to peek.")
            return None
        return self.array[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.MAX_SIZE - 1


class ArrayDownStack(Stack):
    def __init__(self):
        self.array = []
        self.top = 4  # Start from the end of the array
        self.MAX_SIZE = 5

    def push(self, element):
        if self.is_full():
            print(f"Stack is full. Cannot push element: {element}")
            return
        self.array.insert(self.top, element)
        self.top -= 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop element.")
            return None
        popped = self.array[self.top + 1]
        del self.array[self.top + 1]
        self.top += 1
        return popped

    def element(self):
        if self.is_empty():
            print("Stack is empty. No element to peek.")
            return None
        return self.array[self.top + 1]

    def is_empty(self):
        return self.top == 4

    def is_full(self):
        return self.top == -1

