# Take an integer input from the user (e.g., input("Enter a number: ")).
# Convert this input to an integer type.
# Multiply it by 5 and print the result.
# Convert the original input to a float and print its type.

integer = int(input("Enter The Value :"))

print(f"Multiple by 5 :{integer * 5} Type : {type(integer)}")

float = float(integer)

print(f"Original Value into Float Number : {float} Type : {type(float)}")
