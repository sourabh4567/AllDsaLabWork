# ---------------------------------------------
# Inventory Stock Manager - Process Sales + Zero Stock Detection
# ---------------------------------------------


def process_sale(inventory, sku, qty_sold):
    """
    Decrease stock of specific SKU based on sales.
    - If SKU not found, notify user.
    - If stock is insufficient, notify user.

    Args:
        inventory (list of tuples): [(SKU, quantity), ...]
        sku (int): SKU identifier to process sale
        qty_sold (int): Quantity sold

    Returns:
        updated_inventory (list of tuples)
    """

    updated_inventory = []     # create new updated list
    sku_found = False

    for item in inventory:
        current_sku, current_qty = item

        if current_sku == sku:
            sku_found = True

            # Case 1: Sufficient stock
            if current_qty >= qty_sold:
                updated_inventory.append((current_sku, current_qty - qty_sold))
                print(f"Sale processed: {qty_sold} units of SKU {sku}.")
            else:
                # Case 2: Insufficient stock
                updated_inventory.append((current_sku, current_qty))
                print(f"Insufficient stock for SKU {sku}. Available: {current_qty}")

        else:
            updated_inventory.append(item)

    # Case 3: SKU not found
    if not sku_found:
        print(f"SKU {sku} not found in inventory.")

    return updated_inventory



def identify_zero_stock(inventory):
    """
    identify all SKUs with zero stock.

    Args:
        inventory (list of tuples): [(SKU, quantity), ...]

    Returns:
        zero_stock_list (list of int): SKUs with zero quantity
    """

    zero_stock_list = [sku for sku, qty in inventory if qty == 0]

    if zero_stock_list:
        print(f"Zero stock SKUs: {zero_stock_list}")
    else:
        print("No zero stock items found.")

    return zero_stock_list



# ---------------------------------------------
# Example Test Execution
# ---------------------------------------------
if __name__ == "__main__":

    print("\n--- TC1: Normal Sale ---")
    inventory = [(101, 50)]
    inventory = process_sale(inventory, 101, 30)
    print("Updated Inventory:", inventory)

    print("\n--- TC2: Insufficient Stock ---")
    inventory = [(102, 20)]
    inventory = process_sale(inventory, 102, 25)
    print("Updated Inventory:", inventory)

    print("\n--- TC3: SKU Not Found ---")
    inventory = [(101, 50)]
    inventory = process_sale(inventory, 104, 10)
    print("Updated Inventory:", inventory)

    print("\n--- TC4: Zero Stock Detection ---")
    inventory = [(101, 0), (102, 5), (103, 0)]
    zero_stock_items = identify_zero_stock(inventory)

    print("\n--- TC5: No Zero Stock ---")
    inventory = [(101, 10), (102, 5)]
    zero_stock_items = identify_zero_stock(inventory)

    print("\n--- TC6: Sale Reducing to Zero ---")
    inventory = [(101, 10)]
    inventory = process_sale(inventory, 101, 10)
    print("Updated Inventory:", inventory)
