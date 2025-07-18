# *args and **kwargs
def sum_all_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of multiple numbers:", sum_all_numbers(1, 2, 3, 4, 5))

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Vashu", age=25, city="Uttar Pradash")