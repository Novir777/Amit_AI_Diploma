def calculator():
    """
    A simple calculator program that performs basic arithmetic operations.
    """
    print("Welcome to the Basic Calculator!")

    while True:
        # Display operation menu
        print("\nPlease select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Get user choice with validation
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice not in range(1, 6):
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Exit if user chooses option 5
        if choice == 5:
            print("Thank you for using the Basic Calculator. Goodbye!")
            break

        # Get the two numbers for calculation with validation
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform the selected operation
        if choice == 1:  # Addition
            result = num1 + num2
            operation = "adding"
        elif choice == 2:  # Subtraction
            result = num1 - num2
            operation = "subtracting"
        elif choice == 3:  # Multiplication
            result = num1 * num2
            operation = "multiplying"
        elif choice == 4:  # Division
            # Check for division by zero
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2
            operation = "dividing"

        # Display the result
        print(f"The result of {operation} {num1} and {num2} is {result}")

        # Ask if the user wants to perform another calculation
        continue_calc = input(
            "\nDo you want to perform another calculation? (yes/no): ").lower()
        if continue_calc != "yes":
            print("Thank you for using the Basic Calculator. Goodbye!")
            break


# Run the calculator
if __name__ == "__main__":
    calculator()
