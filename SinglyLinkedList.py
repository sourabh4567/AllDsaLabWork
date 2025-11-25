# -------------------------------------------------
# Node Class
# -------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# -------------------------------------------------
# Singly Linked List Class
# -------------------------------------------------
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at beginning.")

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:    # Empty list
            self.head = new_node
        else:
            temp = self.head
            while temp.next:     # Traverse to last node
                temp = temp.next
            temp.next = new_node
        print(f"Inserted {data} at end.")

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # Case 1: Empty list
        if temp is None:
            print("List is empty. Nothing to delete.")
            return

        # Case 2: Node to delete is head
        if temp.data == key:
            self.head = temp.next
            print(f"Deleted {key} from list.")
            return

        # Case 3: Node somewhere in the list
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"{key} not found in list.")
        else:
            prev.next = temp.next
            print(f"Deleted {key} from list.")

    # Search for a node
    def search(self, key):
        temp = self.head
        position = 1
        while temp:
            if temp.data == key:
                print(f"{key} found at position {position}.")
                return True
            temp = temp.next
            position += 1
        print(f"{key} not found in the list.")
        return False

    # Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------------------------------------------------
# Example Usage
# -------------------------------------------------

ll = SinglyLinkedList()

ll.insert_begin(10)
ll.insert_begin(20)
ll.insert_end(30)
ll.insert_end(40)

ll.display()

ll.search(30)
ll.search(99)

ll.delete(20)
ll.delete(99)

ll.display()
