#main.py
import basic_operations as basic
import advanced_operations as advanced
import trig_functions as trig
import memory_functions as memory
import history

def main():
    print("Welcome to the Multi-Operation Calculator")
    history.clear_history()
    
    while True:
        print("\nOptions:")
        print("1. Basic Operations")
        print("2. Advanced Operations")
        print("3. Trigonometric Functions")
        print("4. Memory Functions")
        print("5. View History")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            basic.handle_basic_operations()
        elif choice == '2':
            advanced.handle_advanced_operations()
        elif choice == '3':
            trig.handle_trig_functions()
        elif choice == '4':
            memory.handle_memory_functions()
        elif choice == '5':
            history.view_history()
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        
if __name__ == "__main__":
    main()

#end of main.py


#basic_operations.py    
import history

def add(a, b):
    result = a + b
    history.add_to_history(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    history.add_to_history(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    history.add_to_history(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    if b != 0:
        result = a / b
        history.add_to_history(f"{a} / {b} = {result}")
        return result
    else:
        history.add_to_history("Division by zero error")
        return "Error: Division by zero"

def handle_basic_operations():
    print("Basic Operations:")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    
    if operation == '+':
        print(f"Result: {add(a, b)}")
    elif operation == '-':
        print(f"Result: {subtract(a, b)}")
    elif operation == '*':
        print(f"Result: {multiply(a, b)}")
    elif operation == '/':
        print(f"Result: {divide(a, b)}")
    else:
        print("Invalid operation.")

#end of basic_operations.py


#advanced operations.py
import math
import history

def power(base, exponent):
    result = math.pow(base, exponent)
    history.add_to_history(f"{base} ^ {exponent} = {result}")
    return result

def sqrt(number):
    result = math.sqrt(number)
    history.add_to_history(f"sqrt({number}) = {result}")
    return result

def factorial(number):
    result = math.factorial(number)
    history.add_to_history(f"{number}! = {result}")
    return result

def handle_advanced_operations():
    print("Advanced Operations:")
    print("1. Power")
    print("2. Square Root")
    print("3. Factorial")
    
    choice = input("Choose operation: ")
    
    if choice == '1':
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print(f"Result: {power(base, exponent)}")
    elif choice == '2':
        number = float(input("Enter number: "))
        print(f"Result: {sqrt(number)}")
    elif choice == '3':
        number = int(input("Enter number: "))
        print(f"Result: {factorial(number)}")
    else:
        print("Invalid operation.")
#end of advanced_operations.py

#trig_function.py
import math
import history

def sine(angle):
    result = math.sin(math.radians(angle))
    history.add_to_history(f"sin({angle}) = {result}")
    return result

def cosine(angle):
    result = math.cos(math.radians(angle))
    history.add_to_history(f"cos({angle}) = {result}")
    return result

def tangent(angle):
    result = math.tan(math.radians(angle))
    history.add_to_history(f"tan({angle}) = {result}")
    return result

def handle_trig_functions():
    print("Trigonometric Functions:")
    angle = float(input("Enter angle in degrees: "))
    operation = input("Choose operation (sin, cos, tan): ")
    
    if operation == 'sin':
        print(f"Result: {sine(angle)}")
    elif operation == 'cos':
        print(f"Result: {cosine(angle)}")
    elif operation == 'tan':
        print(f"Result: {tangent(angle)}")
    else:
        print("Invalid operation.")
#end of trig_functions.py

#memory_functions.py
memory_storage = None

def store_value(value):
    global memory_storage
    memory_storage = value

def recall_value():
    return memory_storage

def handle_memory_functions():
    print("Memory Functions:")
    print("1. Store Value")
    print("2. Recall Value")
    
    choice = input("Choose operation: ")
    
    if choice == '1':
        value = float(input("Enter value to store: "))
        store_value(value)
        print("Value stored successfully.")
    elif choice == '2':
        value = recall_value()
        if value is not None:
            print(f"Recalled value: {value}")
        else:
            print("No value stored.")
    else:
        print("Invalid operation.")
#end of memory_functions.py

#history.py

operation_history = []

def add_to_history(operation):
    operation_history.append(operation)

def view_history():
    if operation_history:
        print("Operation History:")
        for operation in operation_history:
            print(operation)
    else:
        print("No history available.")

def clear_history():
    global operation_history
    operation_history = []

#end of history.py




