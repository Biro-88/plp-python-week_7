
# Shopping List Manager

## Assignment Description

This project is a Python Shopping List Manager that demonstrates how to create, access, update, and process lists. It includes three programs that practice list operations, user interaction, membership checking, loops, and simple reporting.

## Files and Their Functions

### 1. list_warmup.py
Demonstrates how to create a list, access the first and last elements using indexes, add items using append(), remove items using remove(), and count items using len().

### 2. shopping_list.py
Creates an interactive shopping list manager. Users can add items, remove existing items, display all items, and exit the program using a menu. It checks whether an item exists before removing it and handles invalid commands without crashing.

### 3. list_report.py
Prints a numbered shopping list, counts the item names containing more than four characters, and finds the longest item name using a loop and length comparison.

### 4. screenshots/
Contains screenshots showing the output of all three Python programs running.

## Why Is It Safer to Check `in` Before Calling `.remove()`?

Checking whether an item is in a list before calling remove() makes the program safer because remove() raises a ValueError if the item does not exist. Using the in operator allows the program to check whether the item is present before attempting to remove it. If the item is missing, the program can display a helpful message instead of crashing.

## How to Run the Programs

Open the terminal in the project folder and run each command:

```bash
python list_warmup.py
```

```bash
python shopping_list.py
```

```bash
python list_report.py
```

## Conclusion

This assignment helped me practice Python lists, indexing, append(), remove(), membership testing with in, loops, conditional statements, and the len() function. These skills are useful for building programs that manage collections of information.
