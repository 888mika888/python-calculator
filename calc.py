import time

# math functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("This is my Calculator")
print("\nChoose an Operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# calc runs till exit()
while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            # float for decimals
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))

            if choice == '4' and num2 == 0:
                print("Error: Cannot divide by zero.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # user asked for another calculation or to exit
        while True:
            next_calc = input("Do another one? (y/n): ").strip().lower()
            if next_calc == 'y':
                break
            elif next_calc == 'n':
                print("Bye:D")
                time.sleep(3)
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")