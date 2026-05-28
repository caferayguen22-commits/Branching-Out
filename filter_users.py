import json


def load_users(file_path="users.json"):
    """Lädt die Benutzerdaten aus der JSON-Datei."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []


def filter_users_by_name(name):
    """Filtert Benutzer nach ihrem Namen (Case-Insensitive)."""
    users = load_users()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """Filtert Benutzer nach einem exakten Alter."""
    users = load_users()
    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """Filtert Benutzer nach ihrer E-Mail-Adresse (Case-Insensitive)."""
    users = load_users()
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name/age/email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid number for age.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")