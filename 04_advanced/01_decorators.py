# Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")
    return "Greeting Complete"


@my_decorator
def calculate_sum(a, b):
    return a + b


say_hello("World")
sum_result = calculate_sum(10, 20)
print(f"Calculated sum: {sum_result}")
