# -----------------------------------------
# INVENTORY MANAGEMENT SYSTEM (FULL VERSION)
# Supports all test cases TC01–TC14
# -----------------------------------------

inventory = []
MAX_CAPACITY = 100   # TC11 capacity limit


# ----------------------------
# Insert or Update Product
# ----------------------------
def insert_or_update_product():
    if len(inventory) >= MAX_CAPACITY:
        print("Error: Inventory capacity exceeded!")
        return

    sku = input("Enter SKU: ").strip()

    # Check SKU is not empty
    if sku == "":
        print("Error: SKU cannot be empty.")
        return

    # Search existing SKU (TC13)
    for item in inventory:
        if item["sku"] == sku:
            print("Product exists. Updating quantity instead.")
            try:
                quantity = int(input("Enter new quantity: "))
                if quantity < 0:
                    print("Error: Quantity must be positive.")
                    return
            except ValueError:
                print("Invalid input. Quantity must be a number.")
                return
            item["quantity"] = quantity
            print("Quantity updated successfully.")
            return

    # New Entry
    name = input("Enter Product Name: ").strip()

    if name == "":  # TC07
        print("Error: Product name cannot be empty.")
        return

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:  # TC04
        print("Invalid input. Quantity must be a number.")
        return

    if quantity < 0:  # TC08
        print("Error: Quantity must be positive.")
        return

    # Insert new product
    product = {"sku": sku, "name": name, "quantity": quantity}
    inventory.append(product)
    print("Product inserted successfully.")


# ----------------------------
# Display Inventory
# ----------------------------
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory:")
    print("SKU\t\tName\t\tQuantity")
    print("----------------------------------------")

    for item in inventory:
        print(f"{item['sku']}\t\t{item['name']}\t\t{item['quantity']}")


# ----------------------------
# Search by SKU (TC05)
# ----------------------------
def search_by_sku():
    sku = input("Enter SKU to search: ").strip()

    for item in inventory:
        if item["sku"] == sku:
            print("\nProduct Found:")
            print(f"SKU: {item['sku']}")
            print(f"Name: {item['name']}")
            print(f"Quantity: {item['quantity']}")
            return

    print("Product not found.")


# ----------------------------
# Search by Name (TC06)
# ----------------------------
def search_by_name():
    name = input("Enter Product Name to search: ").strip().lower()

    for item in inventory:
        if item["name"].lower() == name:
            print("\nProduct Found:")
            print(f"SKU: {item['sku']}")
            print(f"Name: {item['name']}")
            print(f"Quantity: {item['quantity']}")
            return

    print("Product not found.")


# ----------------------------
# Delete Product (TC09, TC14)
# ----------------------------
def delete_product():
    sku = input("Enter SKU to delete: ").strip()

    for item in inventory:
        if item["sku"] == sku:
            inventory.remove(item)
            print(f"Product SKU: {sku} removed successfully.")
            return

    print("Product not found.")


# ----------------------------
# Main Menu
# ----------------------------
def main():
    while True:
        print("\n===== INVENTORY STOCK MANAGER =====")
        print("1. Insert/Update Product")
        print("2. Display Inventory")
        print("3. Search by SKU")
        print("4. Search by Name")
        print("5. Delete Product")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            insert_or_update_product()
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            search_by_sku()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1–6.")


# Start the program
main()
