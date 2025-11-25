# ---------------- Fixed-Size Linear Queue ----------------

class TicketQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity   # fixed-size array
        self.front = 0
        self.rear = -1
        self.count = 0                   # number of elements in queue

    # Enqueue (Insert)
    def enqueue(self, request_id):
        if self.isFull():
            print("Queue is full! Cannot add new ticket request.")
            return
        
        self.rear += 1
        self.queue[self.rear] = request_id
        self.count += 1
        print(f"Enqueued Request ID: {request_id}")

    # Dequeue (Delete)
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! No request to process.")
            return
        
        removed = self.queue[self.front]
        print(f"Dequeued Request ID: {removed}")

        self.front += 1
        self.count -= 1
        return removed

    # Check if queue is empty
    def isEmpty(self):
        return self.count == 0

    # Check if queue is full
    def isFull(self):
        return self.count == self.capacity

    # Return size of queue
    def size(self):
        return self.count

    # Display queue
    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Current Queue:", self.queue[self.front:self.rear + 1])


# ----------------------- Menu-Driven Program -----------------------

def main():
    q = TicketQueue(capacity=5)   # fixed-size queue of size 5

    while True:
        print("\n======= Ticket Request Queue =======")
        print("1. Add Ticket Request (Enqueue)")
        print("2. Process Next Request (Dequeue)")
        print("3. Show Queue Size")
        print("4. Check if Queue is Full")
        print("5. Display Queue")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ")

        if choice == '1':
            request_id = input("Enter Ticket Request ID: ")
            q.enqueue(request_id)

        elif choice == '2':
            q.dequeue()

        elif choice == '3':
            print("Current Queue Size:", q.size())

        elif choice == '4':
            print("Is Queue Full? ->", q.isFull())

        elif choice == '5':
            q.display()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter between 1–6.")


# Start Program
if __name__ == "__main__":
    main()
