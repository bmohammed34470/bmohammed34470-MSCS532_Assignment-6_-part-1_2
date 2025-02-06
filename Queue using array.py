class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, value):
        if len(self.queue) < self.max_size:
            self.queue.append(value)
        else:
            raise OverflowError("Queue overflow")

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue

# Usage
max_size = int(input("Enter the maximum size of the queue: "))
queue = Queue(max_size)

print("Choose from the following options:")
print("1. Enqueue Element\n2. Dequeue Element\n3. Check if Queue is Empty\n4. Display Queue")

a = True

while a:
    x = int(input("Enter your option: "))

    if x == 1:
        queue.enqueue(int(input("Enter the element to enqueue: ")))
    elif x == 2:
        print(f"Dequeued element: {queue.dequeue()}")
    elif x == 3:
        print(f"Is queue empty?: {queue.is_empty()}")
    elif x == 4:
        print(f"Queue elements: {queue.display()}")
    else:
        print("Invalid option; exiting...")
        a = False
