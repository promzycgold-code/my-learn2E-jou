set_username = "Admin"
set_password = "admin123"

# Initialize counters
username_attempts = 1
password_attempts = 1

# Step 1: Username checking loop
while username_attempts <= 4:
    username_input = input().capitalize()

    if username_input == set_username:
        print("Username correct!")
        
        # Step 2: Password checking loop (only runs if username is correct)
        while password_attempts <= 4:
            password_input = input(f"Password Attempt {password_attempts}/4: ")
            
            if password_input == set_password:
                print("Login successful! Welcome.")
                break  # Breaks out of the password loop on success
            else:
                print("Error: Incorrect password.")
                password_attempts += 1  # Add 1 to password attempts on failure
                
        # Check if password loop ended due to reaching the max attempts limit
        if password_attempts > 4:
            print("\nError: Too many incorrect password attempts.")
            
        break  # Breaks out of the username loop because validation is complete
        
    else:
        print("Error: Incorrect username.")
        username_attempts += 1  # Add 1 to username attempts on failure

# Check if username loop ended due to reaching the max attempts limit
if username_attempts > 4:
    print("\nError: Too many incorrect username attempts. Account locked.")
