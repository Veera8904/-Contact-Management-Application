contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added.")

def view_contacts():
    if contacts:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts available.")

def update_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(f"Contact '{name}' updated.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            update_contact(name, new_phone)
        elif choice == 4:
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()