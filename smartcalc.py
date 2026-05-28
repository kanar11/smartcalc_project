# SmartCalc Solutions - Modular Calculator
# Author: Kasper Kanarek
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