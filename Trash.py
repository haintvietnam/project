import json

# Function to load users from a JSON file
def load_users(filename):
    with open(filename, 'r',) as file:
        data = json.load(file)
    return data['users']

# Function to check login credentials
def login(users, username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

# Main function
def main():
    # Load users from the JSON file
    users = load_users('data/tai_khoan_nguoi_dung.json')

    # Ask for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check login credentials
    if login(users, username, password):
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")

if __name__ == "__main__":
    main()

