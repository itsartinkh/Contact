#!/usr/bin/env python3
"""
Contact Book CLI App

Features:
- Add new contacts (name, phone, email)
- View all contacts
- Search for a contact by name
- Delete a contact
- Save & load contacts from a JSON file
"""

import json
import os

CONTACTS_FILE = "contacts.json"


# -----------------------------
# Helper functions
# -----------------------------
def load_contacts():
    """Load contacts from file (if it exists)."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    """Save contacts to file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def display_contacts(contacts):
    """Show all saved contacts."""
    if not contacts:
        print("\n📂 No contacts found.\n")
        return
    print("\n📂 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact.get('address', 'N/A')}")


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print(f"✅ Contact {name} added successfully!\n")

def search_contact(contacts):
    """Search contacts by name or phone."""
    #this function allows the user to search for contacts by name or phone number.
    keyword = input("Enter name or phone to search: ").lower()
    results = [c for c in contacts if keyword in c['name'].lower() or keyword in c['phone']]

    if results:
        print("\n🔎 Search Results:")
        for c in results:
            print(f"- {c['name']} | {c['phone']} | {c['email']}")
        print()
    else:
        print("❌ No contacts found matching your search.\n")


def delete_contact(contacts):
    """Delete a contact by name."""
    name = input("Enter the name of the contact to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            save_contacts(contacts)
            print(f"🗑️ Contact {name} deleted successfully!\n")
            print()  # <--- خط جدید
            return
    print("❌ Contact not found.\n")


def update_contact(contacts):
    """Update a contact's phone number by name."""
    name = input("Enter the name of the contact to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            new_phone = input("Enter new phone number: ")
            c['phone'] = new_phone
            save_contacts(contacts)
            print(f"✅ Contact {name} updated successfully!\n")
            return
    print("❌ Contact not found.\n")

# -----------------------------
# Main menu
# -----------------------------
def main():
    contacts = load_contacts()

    while True:
        print("===== CONTACT BOOK =====")
        print("1. View all contacts")
        print("2. Add new contact")
        print("3. Search contact by name/phone")
        print("4. Delete contact")
        print("5. Update contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            print("👋 Goodbye!")
            break

if __name__ == "__main__":

    main()
