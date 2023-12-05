from PythonLab3.stack.array_stack import ArrayUpStack
from PythonLab3.stack.linked_stack import LinkedStack
from PythonLab3.queue.array_queue import ArrayQueue
from PythonLab3.queue.linked_queue import LinkedQueue

array_stack = ArrayUpStack()
linked_stack = LinkedStack()


def main():

    queue_or_stack = input("Choose the stack type (1 for ArrayUpStack, 2 for LinkedStack): ")

    if queue_or_stack == "1":
        stack = ArrayUpStack()
    elif queue_or_stack == "2":
        stack = LinkedStack()
    else:
        print("Invalid choice. Exiting.")
        return

    stack_type = input("Choose the stack type (1 for ArrayUpStack, 2 for LinkedStack): ")

    if stack_type == "1":
        stack = ArrayUpStack()
    elif stack_type == "2":
        stack = LinkedStack()
    else:
        print("Invalid choice. Exiting.")
        return

    while True:
        print("\nOptions:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty?")
        print("5. Is Full?")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            element = input("Enter the element to push: ")
            stack.push(element)
        elif choice == "2":
            popped = stack.pop()
            if popped is not None:
                print(f"Popped element: {popped}")
        elif choice == "3":
            peeked = stack.element()
            if peeked is not None:
                print(f"Top element: {peeked}")
        elif choice == "4":
            print(f"Is Empty? {stack.is_empty()}")
        elif choice == "5":
            print(f"Is Full? {stack.is_full()}")
        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

        # Choose the type of queue (ArrayQueue or LinkedQueue)
        queue_type = input("Choose the queue type (1 for ArrayQueue, 2 for LinkedQueue): ")

        if queue_type == "1":
            queue = ArrayQueue()
        elif queue_type == "2":
            queue = LinkedQueue()
        else:
            print("Invalid choice. Exiting.")
            return

        while True:
            print("\nOptions:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Is Empty?")
            print("5. Is Full?")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                element = input("Enter the element to enqueue: ")
                queue.enqueue(element)
            elif choice == "2":
                dequeued = queue.dequeue()
                if dequeued is not None:
                    print(f"Dequeued element: {dequeued}")
            elif choice == "3":
                peeked = queue.peek()
                if peeked is not None:
                    print(f"Front element: {peeked}")
            elif choice == "4":
                print(f"Is Empty? {queue.is_empty()}")
            elif choice == "5":
                print(f"Is Full? {queue.is_full()}")
            elif choice == "0":
                print("Exiting.")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()


