# Print numbers from 1 to 20.
# Use continue to skip printing numbers that are multiples of 3.
# Use break to stop the loop if the number reaches 15.Print numbers from 1 to 20.
# Use continue to skip printing numbers that are multiples of 3.
# Use break to stop the loop if the number reaches 15.

for number in range(1, 21):
    if number == 15:
        print(f"Loop stopped at {number}.")
        break

    if number % 3 == 0:
        print(f"Skipping {number} (multiple of 3)")
        continue

    print(number)
