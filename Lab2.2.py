def linear_search(arr, x):
    steps = 0  # count steps for analysis

    for i in range(len(arr)):
        steps += 1
        if arr[i] == x:
            return i, steps   # return index and steps
    return -1, steps


# Example
arr = [5, 10, 15, 20, 25]

print("Array:", arr)
x = int(input("Enter element to search: "))

index, steps = linear_search(arr, x)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found.")

print(f"Total steps taken: {steps}")
