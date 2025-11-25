# --------------------------------------------------------
# Ticketing System using Linear Queue (Python)
# --------------------------------------------------------

class TicketQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size   # fixed-size linear queue
        self.front = -1
        self.rear = -1

    # Check if queue is full
    def isFull(self):
        return self.rear == self.size - 1

    # Check if queue is empty
    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

    # Add a ticket request (Enqueue)
    def enqueue(self, ticket_id):
        if self.isFull():
            print("Queue is Full! Cannot add more ticket requests.")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = ticket_id
        print(f"Ticket Request Added: {ticket_id}")

    # Process a ticket request (Dequeue)
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty! No ticket to process.")
            return None

        ticket = self.queue[self.front]
        print(f"Ticket Processed: {ticket}")
        self.front += 1
        return ticket

    # Display all pending tickets
    def display(self):
        if self.isEmpty():
            print("No pending ticket requests.")
            return

        print("Pending Tickets:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


# --------------------------------------------------------
# Main Program (Menu Driven)
# --------------------------------------------------------

def main():
    q = TicketQueue(size=5)   # queue can hold 5 ticket requests

    while True:
        print("\n======= Ticketing System =======")
        print("1. Add Ticket Request (Enqueue)")
        print("2. Process Ticket (Dequeue)")
        print("3. Show Pending Tickets")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            ticket_id = input("Enter Ticket ID: ")
            q.enqueue(ticket_id)

        elif choice == "2":
            q.dequeue()

        elif choice == "3":
            q.display()

        elif choice == "4":
            print("Exiting Ticketing System.")
            break

        else:
            print("Invalid choice! Please enter a number between 1-4.")


# Run the program
if __name__ == "__main__":
    main()
