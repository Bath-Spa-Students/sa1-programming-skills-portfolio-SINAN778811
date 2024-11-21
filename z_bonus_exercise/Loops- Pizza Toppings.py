# Establish an infinite loop to ask for pizza toppings
while True:
    toppings = input("Enter a pizza toppings (or type 'quit' to stop): ")

    # Analyze if the user wants to quit
    if toppings.lower() == 'quit':
        break

    # Print a message for each design
    print(f"Adding {toppings} to your pizza!")
