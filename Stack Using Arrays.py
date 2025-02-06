class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, value):
        if len(self.stack) < self.max_size:
            self.stack.append(value)
        else:
            raise OverflowError("Stack overflow")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

# Usage
max_size = int(input("Enter the maximum size of the stack: "))
stack = Stack(max_size)

print("Choose from the following options:")
print("1. Push Element\n2. Pop Element\n3. Peek Element\n4. Check if Stack is Empty\n5. Display Stack")

a = True

while a:
    x = int(input("Enter your option: "))

    if x == 1:
        stack.push(int(input("Enter the element to push: ")))
    elif x == 2:
        print(f"Popped element: {stack.pop()}")
    elif x == 3:
        print(f"Element on top: {stack.peek()}")
    elif x == 4:
        print(f"Is stack empty?: {stack.is_empty()}")
    elif x == 5:
        print(f"Stack elements: {stack.display()}")
    else:
        print("Invalid option; exiting...")
        a = False
