# Create a list fruits = ["apple", "banana", "cherry"].
# Add "orange" to the end of the list.
# Insert "grape" at the second position.
# Remove "banana".
# Print the final list.
# Check if "apple" is in the list and print a boolean result.
# Print the length of the list.

list = ["apple", "banana", "cherry"]

print(f"Original List : {list}")

list.append("grape")

print(f"Grape Add in list : {list}")

list.remove("banana")

print(f"Banana remove form list : {list}")

if list == ['banana']:
    print(f"{bool}")

print(f"Length of List : {len(list)}")