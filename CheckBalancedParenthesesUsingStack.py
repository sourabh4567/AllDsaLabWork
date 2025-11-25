# Function to check balanced parentheses using stack

def is_balanced(expression):
    stack = []
    
    # Dictionary to match closing brackets with their opening brackets
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # Push opening brackets into stack
        if char in "([{":
            stack.append(char)
        
        # If closing bracket encountered
        elif char in ")]}":
            # If stack is empty → no matching opening bracket
            if not stack:
                return False
            
            top = stack.pop()
            if mapping[char] != top:
                return False

    # If stack empty → all parentheses matched correctly
    return len(stack) == 0


# -------------------- Example Usage --------------------
expr = input("Enter an expression: ")

if is_balanced(expr):
    print("Parentheses are balanced.")
else:
    print("Parentheses are NOT balanced.")
