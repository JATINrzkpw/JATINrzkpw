def get_user_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

# Example usage
username, password = get_user_credentials()
print("Username:", username)
print("Password:", password)

