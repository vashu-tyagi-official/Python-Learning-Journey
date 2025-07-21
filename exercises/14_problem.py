# Given numbers = [10, 20, 30, 40, 50, 60, 70].
# Print the first three elements.
# Print elements from the third to the end.
# Print every second element.
# Print the list in reverse order.

numbers = [10, 20, 30, 40, 50, 60, 70]

print(f"First Three Element Of List : {numbers[:3]}")

print(f"last Three Element Of List : {numbers[-3:]}")

print(f"Second Element Of List : {numbers[1]}")

numbers.reverse()

print(f"Reverse Element Of List : {numbers}")