
set_username = "Admin"
set_password = "admin123"


for attempt in range(1, 5):
    
    username_input = input(f"{attempt} Enter username: ").capitalize()

    if username_input == set_username:
        print("Username correct!")
        
        password_input = input("Enter password: ")
        if password_input == set_password:
            print("Login successful! Welcome.")
        else:
            print("Error: Incorrect password. Access denied.")
        break
else:
    print("\nError: Too many incorrect attempts. Account locked.")
