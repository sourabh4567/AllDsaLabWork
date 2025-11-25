# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # point to itself
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head  # maintain circular link

    # Insert node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        # Reach the last node
        while temp.next != self.head:
            temp = temp.next

        # Insert the new node before head
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node  # New node becomes the head

    # Display the circular linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


# ---------------- Example Usage ----------------

cll = CircularLinkedList()

# Insert nodes at end
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)

print("Original list:")
cll.display()

# Insert at beginning
cll.insert_at_beginning(5)
print("\nAfter inserting 5 at beginning:")
cll.display()

# Insert at end
cll.insert_at_end(40)
print("\nAfter inserting 40 at end:")
cll.display()
