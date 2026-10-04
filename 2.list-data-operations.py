# Creating our shopping list
grocery_list = ["Eggs", "Milk", "Bread"]

# Accessing items by their position (Index)
print(grocery_list[0]) 
print(grocery_list[1]) 

# Using negative numbers counts backward from the end
print(grocery_list[-1]) # Output: The very last item


# Adding Items In a List
# 1. append() — Adds an item to the very end of the list
grocery_list.append("Apples")
print(grocery_list) 


# 2. insert() — Adds an item into a specific position
# Syntax: list.insert(position, item)

grocery_list.insert(1, "Butter") 
print(grocery_list)


# Removing Items from a list
# 1. remove() — Deletes an item by its specific name
grocery_list.remove("Milk")
print(grocery_list)

# 2. pop() — Removes an item based on its position number
# This removes whatever is at position 2 ("Bread") and saves it to a variable
removed_item = grocery_list.pop(2) 

print(f"I took this out of the list: {removed_item}")
print(grocery_list)


# Searching and Checking in a List
if "Eggs" in grocery_list:
    print("Yes, you need to buy eggs.")

# Counting the items (len())
# Tells you the total number of items left on your list
print(len(grocery_list))

# Sorting the list alphabetically (sort())
grocery_list.sort()
print(grocery_list) 
# Output: ['Apples', 'Butter', 'Eggs'] (Now it's in A-Z order!)