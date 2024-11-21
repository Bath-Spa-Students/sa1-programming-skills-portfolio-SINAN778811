# Checking the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Adding the search term from the user
search_term = input("Enter the name you want to search for: ")

# check for the name in the list
if search_term in names:
    print(f"{search_term} was found in the list.")
else:
    print(f"{search_term} was not found in the list.")
