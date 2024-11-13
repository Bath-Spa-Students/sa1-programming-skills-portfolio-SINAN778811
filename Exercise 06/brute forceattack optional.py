# Write the correct password
correct_password = "12345"
# Make the maximum number of attempts
max_attempts = 5
# Illustrate attempt counter
attempts = 0

# Loop until the id enters the correct password or reaches the maximum attempts
while attempts < max_attempts:
    # Request the id to enter the password
    password = input("Please enter the password: ")
    
    # Verify the entered password is correct
    if password == correct_password:
        print("Access granted!")
        break
    else:
        # Expansion the attempt counter
        attempts += 1
        remaining_attempts = max_attempts - attempts
        # Brief the id of the incorrect password and remaining attempts
        print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")
        
        # If maximum attempts are reached, update the id
        if attempts == max_attempts:
            print("Maximum attempts reached. The authorities have been alerted.")
