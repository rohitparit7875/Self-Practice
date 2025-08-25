def calculator(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b if b != 0 else "Cannot divide by zero"
    else: return "Invalid operator"

print(calculator(10, 5, '*'))
