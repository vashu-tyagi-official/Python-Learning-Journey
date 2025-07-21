# Ask the user for a positive integer N.
# Calculate the sum of all integers from 1 to N using a for loop.
# Print the sum.
# Ask the user for a positive integer N.

while True:
    try:
        N_str = input("Enter a positive integer N: ")
        N = int(N_str)
        if N > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


total_sum = 0
for i in range(1, N + 1):  # range(1, N + 1)
    total_sum += i

print(f"The sum of integers from 1 to {N} is: {total_sum}")
