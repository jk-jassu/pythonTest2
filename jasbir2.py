
phoneDirectory = {}

print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
print("1. Add a record")
print("2. Search a record")
print("3. Update a record")
print("4. Delete a record")
print("5. Quit")


while True:

    choice = input("Enter your choice (1-5): ")

    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phoneDirectory[name] = phone
        print(name, "was added to the phone directory.")
    
    
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phoneDirectory:
            print("Phone number of", name, "is", phoneDirectory[name])
        else:
            print(name, "was not found in the phone directory.")
    
    
    elif choice == "3":
        name = input("Enter name to update: ")
        if name in phoneDirectory:
            phone = input("Enter new phone number: ")
            phoneDirectory[name] = phone
            print(name, "was updated in the phone directory.")
        else:
            print(name, "was not found in the phone directory.")
    
    
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print(name, "was deleted from the phone directory.")
        else:
            print(name, "was not found in the phone directory.")
    
    
    elif choice == "5":
        print("Exiting the phone directory.")
        break
    
    
    else:
        print("Invalid choice. Please enter a valid choice (1-5).")

