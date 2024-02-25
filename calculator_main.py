import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_logarithm(x):
    return math.log(x)

def power(x, b):
    return x ** b

def menu():
    print("\nScientific Calculator Menu:")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power (x^b)")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            x = float(input("Enter the number to find square root of: "))
            print("Square Root of", x, ":", square_root(x))
        elif choice == '2':
            x = int(input("Enter the number to find factorial of: "))
            print("Factorial of", x, ":", factorial(x))
        elif choice == '3':
            x = float(input("Enter the number to find natural logarithm of: "))
            print("Natural Logarithm of", x, ":", natural_logarithm(x))
        elif choice == '4':
            x = float(input("Enter the base number: "))
            b = float(input("Enter the power: "))
            print(x, "raised to the power", b, ":", power(x, b))
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()

