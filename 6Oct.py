# ------------------- Node Class -------------------
class Node:
    def __init__(self, data):
        self.data = data      # store data
        self.next = None      # pointer to next node


# ---------------- Singly Linked List ----------------
class LinkedList:
    def __init__(self):
        self.head = None      # initially empty list

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head   # new node → old head
        self.head = new_node        # head becomes new node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node        # link last node to new node

    # Search for a value in the linked list
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                print(f"{key} found in the list.")
                return True
            temp = temp.next

        print(f"{key} not found in the list.")
        return False

    # Display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ------------------ Example Usage ------------------
ll = LinkedList()

# Insert nodes
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

# Display linked list
ll.display()

# Search functionality
ll.search(30)   # should print "30 found"
ll.search(99)   # should print "99 not found"
