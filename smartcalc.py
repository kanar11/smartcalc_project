# SmartCalc Solutions - Modular Calculator
# Author: Kasper Kanarek
# Version: 1.0 - Final version
# Features: Addition, Subtraction, Multiplication, Division, Power, Modulo 
# Addition function - adds two numbers and returns the result
def add(a, b):
    return a + b
# Subtraction function - subtracts b from a and returns the result
def subtract(a, b):
    return a - b
# Multiplication function - multiplies two numbers and returns the result
def multiply(a, b):
    return a * b
# Division function - divides a by b, prevents division by zero
def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b
# Power function - raises a to the power of b
def power(a, b):
    return a ** b

# Modulo function - returns remainder of a divided by b
def modulo(a, b):
    return a % b

# Main menu - handles user interaction and calls appropriate functions
def menu():
    while True:
        print("====== SmartCalc Solutions ======")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulo")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "7":
            print("Exiting calculator...")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        elif choice == "5":
            print("Result:", power(a, b))
        elif choice == "6":
            print("Result:", modulo(a, b))
        else:
            print("Invalid choice. Please try again")

menu()