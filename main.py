import os

def display_menu():
    print("Welcome to the SOLID Principles Interactive Demo!")
    print("Please choose a principle to explore:")
    print("1. Single Responsibility Principle (SRP)")
    print("2. Open/Closed Principle (OCP)")
    print("3. Liskov Substitution Principle (LSP)")
    print("4. Interface Segregation Principle (ISP)")
    print("5. Dependency Inversion Principle (DIP)")
    print("6. Exit")

def load_example(principle):
    principle_path = principle
    
    # Each principle has a bad and good example
    bad_example = os.path.join(principle_path, f"bad_{principle.split('-')[1].lower()}.py")
    good_example = os.path.join(principle_path, f"good_{principle.split('-')[1].lower()}.py")
    
    print("\n--- Bad Example ---")
    with open(bad_example, "r") as file:
        print(file.read())
        
    print("\n--- Good Example ---")
    with open(good_example, "r") as file:
        print(file.read())

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            load_example("1-srp")
        elif choice == '2':
            load_example("2-ocp")
        elif choice == '3':
            load_example("3-lsp")
        elif choice == '4':
            load_example("4-isp")
        elif choice == '5':
            load_example("5-dip")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    main()

