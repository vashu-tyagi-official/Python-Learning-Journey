# Set a predefined secret_password.
# Use a while loop to repeatedly ask the user for a password until they enter the correct one.
# Print "Access Granted!" once correct.

secret_password = "Vashu@12121#VT"

password = input("Enter Your Password :")

while password != secret_password:
    print("Invalid Password ! \nTry Again...")
    password = input("Enter Your Password :")

if password == secret_password:
    print("Access Granted !")
