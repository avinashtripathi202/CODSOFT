# Simple Contact List Program in Python

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {'Phone': phone, 'Email': email}
        print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts to show.")
    else:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {info['Phone']}")
            print(f"  Email: {info['Email']}")
            print("-" * 20)

def search_contact():
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name to update: ").strip()
    if name in contacts:
        print("Leave blank to keep existing value.")
        phone = input(f"New phone number (old: {contacts[name]['Phone']}): ").strip()
        email = input(f"New email (old: {contacts[name]['Email']}): ").strip()
        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact List Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
