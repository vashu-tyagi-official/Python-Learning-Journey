# Break and Continue
print("Break Example:")
for i in range(10):
    if i == 5:
        break # Exit the loop
    print(i)

print("\nContinue Example:")
for i in range(10):
    if i % 2 == 0: # Skip even numbers
        continue
    print(i)