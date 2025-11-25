
class CustomStack:
    def __init__(self, size):
        self.arr = [None] * size      
        self.capacity = size
        self.top = -1

    # Push element onto stack
    def push(self, x):
        if self.is_full():
            print("Stack Overflow")
            raise OverflowError("Stack Overflow")
        self.top += 1
        self.arr[self.top] = x

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            raise IndexError("Stack is Empty")
        value = self.arr[self.top]
        self.top -= 1
        return value

    # Check if stack is empty
    def is_empty(self):
        return self.top == -1

    # Check if stack is full
    def is_full(self):
        return self.top == self.capacity - 1

    # Return stack contents as string
    def get_content(self):
        return ''.join(self.arr[:self.top + 1])



def reverse_string(s):
    stack = CustomStack(len(s))
    for ch in s:
        stack.push(ch)

    reversed_s = ''
    while not stack.is_empty():
        reversed_s += stack.pop()

    return reversed_s



def are_brackets_balanced(expr):
    stack = CustomStack(len(expr))
    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if ch == ')' and top_char not in '(':
                return False
            if ch == '}' and top_char not in '{':
                return False
            if ch == ']' and top_char not in '[':
                return False

    return stack.is_empty()



def simulate_undo():
    editor = CustomStack(10)
    editor.push('h')
    editor.push('e')
    editor.push('l')
    print("Current text:", editor.get_content())

    # Undo last character
    editor.pop()
    print("After undo:", editor.get_content())



if __name__ == "__main__":
    print("1. Reversing a String")
    original = "sourabh"
    reversed_str = reverse_string(original)
    print(f"Original: {original} -> Reversed: {reversed_str}\n")

    print("2. Checking Balanced Parentheses")
    expr1 = "{({[]})}"
    expr2 = "{([)]}"
    print(f"Expression '{expr1}' is balanced: {are_brackets_balanced(expr1)}")
    print(f"Expression '{expr2}' is balanced: {are_brackets_balanced(expr2)}\n")

    print("3. Simulating Undo Operations")
    simulate_undo()
