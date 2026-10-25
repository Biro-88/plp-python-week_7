
# Part B: Shopping List Manager

# 1. Start with an empty shopping list
shopping_list = []

# 2. Display the menu repeatedly
while True:
    print("\n Shopping List Manager")
    print("add / remove / show / done")

    choice = input("What would you like to do? ").strip().lower()

    # Add an item
    if choice == "add":
        item = input("Enter the item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(f"{item} has been added to your shopping list.")
        else:
            print("Please enter a valid item name.")

    # Remove an item safely
    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from your shopping list.")
        else:
            print("That item is not on your list.")

    # Display all items
    elif choice == "show":
        if shopping_list:
            print("\nYour shopping list:")

            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    # End the program
    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    # Handle invalid commands
    else:
        print("Invalid choice. Please enter add, remove, show, or done.")
