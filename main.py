# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def perform_math_operations():
    """
    Task 1: Perform basic mathematical operations.
    """
    print("\n--- Task 1: Mathematical Operations ---")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2

        # Handle division by zero
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Undefined (division by zero)"

        print(f"Addition: {addition}")
        print(f"Subtraction: {subtraction}")
        print(f"Multiplication: {multiplication}")
        print(f"Division: {division}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def create_personalized_greeting():
    """
    Task 2: Create a personalized greeting.
    """
    print("\n--- Task 2: Personalized Greeting ---")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name}! Welcome to the Python program.")

def main():
    """
    Main function to display a menu and execute tasks based on user choice.
    """
    while True:
        print("\n=== Python Basic Concepts Assignment ===")
        print("1. Perform Basic Mathematical Operations")
        print("2. Create a Personalized Greeting")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            perform_math_operations()
        elif choice == "2":
            create_personalized_greeting()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
