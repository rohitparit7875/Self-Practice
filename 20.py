# Program to implement key-value pair functionality

def key_value_demo():
    # Initialize an empty dictionary
    data = {}
    
    while True:
        print("\nChoose an option:")
        print("1. Add key-value pair")
        print("2. Retrieve value by key")
        print("3. Display all key-value pairs")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            data[key] = value
            print(f"Key-value pair '{key}: {value}' added successfully!")
        
        elif choice == "2":
            key = input("Enter key to retrieve value: ")
            if key in data:
                print(f"Value for key '{key}': {data[key]}")
            else:
                print(f"Key '{key}' not found.")
        
        elif choice == "3":
            print("All key-value pairs:")
            for key, value in data.items():
                print(f"{key}: {value}")
        
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
key_value_demo()
