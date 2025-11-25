# ----------------- Node Class -----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ----------------- Singly Linked List -----------------
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:          # if empty list
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:    # traverse till last node
            temp = temp.next

        temp.next = new_node            # attach new node at end

    # Search for a value
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"{key} found in the list.")
                return True
            temp = temp.next

        print(f"{key} not found in the list.")
        return False

    # Display entire list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------------- Example Usage ----------------
ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.display()

# Search Tests
ll.search(30)   # should print "30 found in the list."
ll.search(99)   # should print "99 not found in the list."
