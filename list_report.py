
# Part C: List Report

# 1. Create the required list
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 2. Print every item with a number
print("Shopping List:")

number = 1

for item in items:
    print(f"{number}. {item}")
    number += 1

# 3. Count item names with more than four characters
long_name_count = 0

for item in items:
    if len(item) > 4:
        long_name_count += 1

print("Items with more than 4 letters:", long_name_count)

# 4. Find the longest item name using a loop comparison
longest_item = ""

for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print("Longest item name:", longest_item)
