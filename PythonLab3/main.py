from array_stack import ArrayUpStack
from linked_stack import LinkedStack


array_stack = ArrayUpStack()
linked_stack = LinkedStack()

array_stack.push(1)
array_stack.push(2)

linked_stack.push('A')
linked_stack.push('B')

print(array_stack.is_empty())
print(array_stack.element())
print(array_stack.is_full())
print(array_stack.element())
print(linked_stack.pop())
print(linked_stack.pop())
print(linked_stack.pop())

