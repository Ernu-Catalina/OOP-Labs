from array_stack import ArrayStack
from linked_stack import LinkedStack

# Example usage
array_stack = ArrayStack()
linked_stack = LinkedStack()

array_stack.push(1)
array_stack.push(2)

linked_stack.push('A')
linked_stack.push('B')

print(array_stack.peek())  # Output: 2
print(linked_stack.pop())  # Output: B
