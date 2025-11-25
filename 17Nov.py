# ------------------------------------
# Node structure
# ------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert nodes at the end
    def insert(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Make circular
            return

        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Display the CLL
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        print("Circular Linked List:", end=" ")
        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("(back to head)")

    # Delete node from beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            print("Deleted the only node in the list.")
            return

        # Find last node
        last = self.head
        while last.next != self.head:
            last = last.next

        # Adjust links
        last.next = self.head.next
        self.head = self.head.next

        print("Node deleted from beginning.")

    # Delete node from end
    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            print("Deleted the only node in the list.")
            return

        temp = self.head
        prev = None

        # Traverse to last node
        while temp.next != self.head:
            prev = temp
            temp = temp.next

        # Now 'temp' is last node, 'prev' is second last
        prev.next = self.head
        print("Node deleted from end.")


# ------------------------------------
# Main Program Execution
# ------------------------------------
cll = CircularLinkedList()

# Insert elements
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

print("Initial List:")
cll.display()

# Delete from beginning
cll.delete_begin()
cll.display()

# Delete from end
cll.delete_end()
cll.display()
