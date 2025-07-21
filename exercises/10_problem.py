# Ask the user for a number.
# Print its multiplication table up to 10 (e.g., 5 x 1 = 5, 5 x 2 = 10, ...).

num = int(input("Enter The number :"))

if num < 0:
    raise ValueError("Enter Postitve Integer !")

for i in range(10):
    if num == 0:
        print("Zero is not vaild !")
        break
    else:
        print(f"{num} x {i} = {num * i}")
