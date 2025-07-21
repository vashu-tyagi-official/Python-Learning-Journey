# Ask the user for their score (0-100).
# Use if-elif-else to assign a grade:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# Handle invalid scores (e.g., <0 or >100) by printing "Invalid score."

number = int(input("Enter your number B/W 0 to 100 :"))

if number < 0 or number > 100:
    raise ValueError("Enter Valid Numbers !")
if number >= 90:
    print("A Grade")
elif number >= 80:
    print("B Grade")
elif number >= 70:
    print("C Grade")
elif number >= 60:
    print("D Grade")
else:
    print("Fail !")
