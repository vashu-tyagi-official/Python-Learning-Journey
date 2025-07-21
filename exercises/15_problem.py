coordinates = (10.0, 20.5)

print(f"Original tuple: {coordinates}")

print(f"First element: {coordinates[0]}")

print("\nAttempting to change the second element (this will cause an error):")

try:
    coordinates[1] = 25.0  # This line will raise a TypeError  # type:ignore
except TypeError as e:
    print(f"Caught an error: {e}")
    print(
        "This error occurs because tuples are immutable (their elements cannot be changed after creation)."
    )

x, y = coordinates
print(f"\nTuple unpacked: x = {x}, y = {y}")
print(f"Type of x: {type(x)}, Type of y: {type(y)}")
