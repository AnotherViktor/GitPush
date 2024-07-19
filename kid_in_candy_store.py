# The list of candies to choose from
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected
candy_cart = []

# Print out options for the user to choose from
print("Available candies:")
for index, candy in enumerate(candy_list):
    print(f"[{index}] {candy}")

# Prompt the user to select candies
print("\nPlease select candies by entering their corresponding numbers.")
for _ in range(allowance):
    selected_index = input("Enter the number of the candy you want to select (0-8): ")

    # Check if the input is a valid number
    if selected_index.isdigit():
        selected_index = int(selected_index)
        # Check if the selected index is within the valid range
        if 0 <= selected_index < len(candy_list):
            candy_cart.append(candy_list[selected_index])
            print(f"Added '{candy_list[selected_index]}' to your cart.")
        else:
            print("Invalid number. Please enter a number between 0 and 8.")
    else:
        print("Invalid input. Please enter a valid number.")

# Print the final selection
print("\nYour selected candies:")
print(candy_cart)
