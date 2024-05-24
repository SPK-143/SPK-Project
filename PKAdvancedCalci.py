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
    
import history

def add(a, b):
    result = a + b
    history.add_to_history(f"{a} + {b} = {result}")
    return result
