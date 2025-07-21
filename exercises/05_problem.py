# Ask the user to enter an integer.
# Print whether the number is "Even" or "Odd".

value = int(input("Enter the value to check 'EVEN' or 'ODD' :"))
if value % 2 == 0:
    print(f"EVEN {value}")
else:
    print(f"ODD {value}")
