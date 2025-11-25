# ------------------------------
# Linear Search in Python
# ------------------------------

def linear_search(arr, target):
    """
    Perform Linear Search on the array.
    Returns index if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # element found
    return -1  # element not found


# ------------------------------
# Example Usage
# ------------------------------

arr = [10, 20, 30, 40, 50]
print("Array:", arr)

target = int(input("Enter the element to search: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
