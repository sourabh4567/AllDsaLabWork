# Reverse a string using stack in Python

def reverse_string_using_stack(input_string):
    stack = []

    # Push each character onto the stack
    for ch in input_string:
        stack.append(ch)

    reversed_string = ""

    # Pop characters from stack to reverse the string
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# ----------- Example Usage ------------
string = input("Enter a string to reverse: ")
print("Original String:", string)

reversed_str = reverse_string_using_stack(string)
print("Reversed String:", reversed_str)
