# ---------------------------------------------
# Browser History Navigation System using Stacks
# ---------------------------------------------

# Two stacks: one for back history, one for forward history
back_stack = []
forward_stack = []
current_page = None


def visit_page(page):
    global current_page

    if current_page is not None:
        back_stack.append(current_page)     # push current page to back history

    current_page = page                     # visit new page
    forward_stack.clear()                   # clear forward history
    print(f"Visited: {current_page}")


def go_back():
    global current_page

    if not back_stack:
        print("No pages to go back to.")
        return

    forward_stack.append(current_page)      # push current page to forward stack
    current_page = back_stack.pop()         # pop from back stack
    print(f"Back to: {current_page}")


def go_forward():
    global current_page

    if not forward_stack:
        print("No pages to go forward to.")
        return

    back_stack.append(current_page)         # push current page to back history
    current_page = forward_stack.pop()      # pop from forward stack
    print(f"Forward to: {current_page}")


def show_history():
    print("\n--- Browser History ---")
    print("Back Stack:", back_stack)
    print("Current Page:", current_page)
    print("Forward Stack:", forward_stack)
    print("------------------------\n")


# -------------------------------
# Menu-driven program
# -------------------------------

while True:
    print("\n1. Visit New Page")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        page = input("Enter page URL or name: ")
        visit_page(page)

    elif choice == "2":
        go_back()

    elif choice == "3":
        go_forward()

    elif choice == "4":
        show_history()

    elif choice == "5":
        print("Exiting Browser Navigation System.")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
