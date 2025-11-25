# -----------------------------------------
# Node Class
# -----------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# -----------------------------------------
# Circular Linked List Class
# -----------------------------------------
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the end of CLL
    def insert(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print(f"Inserted {data} (first node).")
            return

        # Otherwise, travel to last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        print(f"Inserted {data} at end.")

    # Search for a value in CLL
    def search(self, key):
        if self.head is None:
            print("List is empty.")
            return False

        temp = self.head
        pos = 1

        while True:
            if temp.data == key:
                print(f"{key} found at position {pos}.")
                return True
            temp = temp.next
            pos += 1

            if temp == self.head:
                break

        print(f"{key} not found in the list.")
        return False

    # Delete a node by value
    def delete(self, key):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        current = self.head
        prev = None

        # Case 1: Only one node
        if current.data == key and current.next == self.head:
            self.head = None
            print(f"Deleted {key} (only node).")
            return

        # Case 2: Deleting head node
        if current.data == key:
            # Move to the last node
            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            print(f"Deleted {key} from beginning.")
            self.head = self.head.next
            return

        # Case 3: Deleting any middle/end node
        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                print(f"Deleted {key} from list.")
                return
            prev = curr
            curr = curr.next

        print(f"{key} not found in the list.")

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        print("Circular Linked List:", end=" ")
        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("(back to head)")


# -----------------------------------------
# Example Usage
# -----------------------------------------
cll = CircularLinkedList()

cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

cll.display()

cll.search(30)
cll.search(99)

cll.delete(10)
cll.delete(30)

cll.display()
