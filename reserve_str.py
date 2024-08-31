def reverse_string(s: str) -> str:
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack to reverse the string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

enter_str = "hello"
output_str = reverse_string(enter_str)
print(output_str)  
