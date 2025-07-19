# my_module.py
def circle_area(radius):
    import math
    return math.pi * radius**2

def greet_user(name):
    return f"Greetings from my_module, {name}!"

if __name__ == "__main__":
    print("This is my_module being run directly.")
    print(f"Area of circle with radius 5: {circle_area(5)}")