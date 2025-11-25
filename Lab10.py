# ------------------------------------
# Binary Search Implementation in Python
# ------------------------------------

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is at mid
        if arr[mid] == target:
            return mid
        
        # If target is smaller, ignore right half
        elif target < arr[mid]:
            right = mid - 1
        
        # If target is larger, ignore left half
        else:
            left = mid + 1

    return -1  # element not found


# ------------------------------------
# Example Usage
# ------------------------------------
arr = [10, 20, 30, 40, 50, 60, 70]   # Sorted list
print("Array:", arr)

target = int(input("Enter element to search: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found.")
