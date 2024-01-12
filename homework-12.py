# 1
"""
def is_admin(func):
    def wrapper(user_type):
        if user_type != 'admin':
            raise ValueError("Permission denied")
        return func(user_type)
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    return "Receipt shown successfully"
"""

# 2
"""
def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as i:
            print(f"Found 1 error during execution of your function: KeyError no such key as {i}")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])
"""
# 3
"""
def check_types(func):
    def wrapper(a, b):
        try:
            if type(a) is int and type(b) is int:
                return func(a, b)
            else:
                return TypeError(f"Arguments must be int, got {type(a)} and {type(b)}")
        except TypeError as i:
            print(i)
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b
"""