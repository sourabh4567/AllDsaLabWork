# -----------------------------------
# Circular Queue Implementation in Python
# -----------------------------------

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check if queue is full
    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    # Check if queue is empty
    def isEmpty(self):
        return self.front == -1

    # Enqueue Operation
    def enqueue(self, value):
        if self.isFull():
            print("Queue is full.")
            return

        if self.front == -1:  # First element
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued: {value}")

    # Dequeue Operation
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return None

        removed = self.queue[self.front]

        if self.front == self.rear:  # Only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {removed}")
        return removed

    # Display the queue
    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
            return

        print("Circular Queue Elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# -----------------------
# Example Usage
# -----------------------
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.display()

cq.dequeue()
cq.dequeue()

cq.display()

cq.enqueue(50)
cq.enqueue(60)

cq.display()
