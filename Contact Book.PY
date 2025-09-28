contacts = []  # This list will store all contacts as dictionaries

# 1. Function to add a new contact
def add_contact():
    name = input("👤 Enter name: ")
    phone = input("📞 Enter phone number: ")
    email = input("📧 Enter email: ")
    address = input("🏠 Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully.")

# 2. Function to view all contacts
def view_contacts():
    if not contacts:
        print("⚠️ No contacts found.")
        return

    print("\n📒 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

# 3. Function to search for a contact by name or phone
def search_contact():
    search = input("🔍 Search by name or phone number: ")
    found = False

    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print("\n✅ Contact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("❌ Contact not found.")

# 4. Function to update a contact's details
def update_contact():
    name = input("✏️ Enter the name of the contact to update: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("🔁 Enter new details (leave blank to keep old data):")
            new_phone = input("New phone number: ") or contact['phone']
            new_email = input("New email: ") or contact['email']
            new_address = input("New address: ") or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address

            print("✅ Contact updated successfully.")
            return

    print("❌ No such contact found.")

# 5. Function to delete a contact
def delete_contact():
    name = input("🗑️ Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("✅ Contact deleted successfully.")
            return

    print("❌ No such contact found.")

# 6. Main menu loop
def main():
    while True:
        print("\n📱 Contact Book Menu:")
        print("1. Add new contact")
        print("2. View contact list")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit program")

        choice = input("👉 Your choice (1-6): ")

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
            print("👋 Thanks! Exiting the app.")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

# Start the program
main()
1