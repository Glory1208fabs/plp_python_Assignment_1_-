def calculator():
    try:
        
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ").strip()

        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose from +, -, *, or /.")
            return

        # Display result
        print(f"The result of {num1} {operation} {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator function
calculator()
