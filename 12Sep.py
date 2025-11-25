# ---------------- STACK OPERATIONS PROGRAM ----------------

stack = []

def push():
    item = input("Enter item to push: ")
    stack.append(item)
    print(f"Pushed {item}")

def pop_item():     # renamed to avoid conflict with built-in pop()
    if not stack:
        print("Stack is empty.")
    else:
        popped = stack.pop()
        print(f"Popped {popped}")

def peek():
    if not stack:
        print("Stack is empty.")
    else:
        print(f"Top item is {stack[-1]}")

def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack items:", stack)


# MAIN MENU
while True:
    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        push()
    elif choice == "2":
        pop_item()
    elif choice == "3":
        peek()
    elif choice == "4":
        display()
    elif choice == "5":
        print("Exiting.")
        break
    else:
        print("Invalid choice, please try again.")
