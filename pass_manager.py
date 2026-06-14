from getpass import getpass
import json ;import random ;import string

DATABASE = "passwords.json"


def load_data():
    try:
        with open(DATABASE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


def save_data(data):
    with open(DATABASE, "w") as file:
        json.dump(data, file, indent=4)


def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = getpass("Password: ")

    data = load_data()

    data[website] = {
        "username": username,
        "password": password
    }

    save_data(data)

    print("Password saved successfully!")


def view_password():
    website = input("Website: ")

    data = load_data()

    if website in data:
        print("\nUsername:", data[website]["username"])
        print("Password:", data[website]["password"])

    else:
        print("No entry found.")

def generate_password(length=12):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    return password

while True:

    print("\nPASSWORD MANAGER")
    print("1. Add Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_password()

    elif choice == "3":
      print("\nGenerated Password:")
      print(generate_password())
    elif choice == "4":
        print("Thank you!")
    break
else:
        print("Invalid choice")