# ---------------------------
# Bubble Sort in Python
# ---------------------------

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):

        # Last i elements are already sorted
        for j in range(0, n - i - 1):

            # Swap if the element found is greater than next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ---------------------------
# Example Usage
# ---------------------------
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted Array:", sorted_arr)
