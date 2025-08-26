def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %, ** (power), exit to quit")
    
    while True:
        op = input("\nEnter operation (+, -, *, /, %, **, exit): ").strip()
        if op.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue

        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            print(f"Result: {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")
        elif op == '%':
            print(f"Result: {num1 % num2}")
        elif op == '**':
            print(f"Result: {num1 ** num2}")
        else:
            print("Invalid operation!")

calculator()
