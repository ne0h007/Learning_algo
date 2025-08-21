'''
Here we will discuss all types of decorators. Below are ones
1) simple decorator
2) decorator with arguments
3) multiple decorators
4) class decorator
5) functools.wrap usage
'''

import time
from functools import wraps

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"total execution time is {end-start}")
        return res
    return wrapper
@time_func
def print_name_five_times(name=None):
    for i in range(5):
        time.sleep(2)
        print(name)

# print_name_five_times('sachin')

def counter_decorator(count_number=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count_number):
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@counter_decorator(count_number=7)
def say_hello(name=None):
    print(f'hello {name}')

# say_hello('sachin')

@time_func
@counter_decorator(count_number=7)
def say_hello(name=None):
    print(f'hello {name}')

# say_hello('sachin')

class MyDecorator:
    def __init__(self,func):
        self.func = func
    
    def __call__(self, *args, **kwds):
        print('class Decorator')
        res = self.func(*args, **kwds)
        return res

@MyDecorator
def say_hello(name=None):
    print(f'hello {name}')


# class decorator with parameter

class MyDecorator_with_params:
    def __init__(self, count_number = None):
        self.count_number = count_number
    def __call__(self, func):
        def wrapper(*args, **kwds):
            for i in range(self.count_number):
                res = func(*args, **kwds)
            return res
        return wrapper
        

@MyDecorator_with_params(count_number=5)
def add_numbers(a=None, b=None):
    res = a+b
    print(res)

# add_numbers(a=5,b=8)


'''
we use functools.wrap so we can fetch wrapped function details. cause without using it we lost these details
'''

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"total execution time is {end-start}")
        return res
    return wrapper
@time_func
def print_name_five_times(name=None):
    '''
    print a name variable five times
    '''
    for i in range(5):
        time.sleep(2)
        print(name)

print(print_name_five_times.__doc__)  # None
print(print_name_five_times.__name__) # wrapper


''' But if we use functools.wrap then '''

def time_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"total execution time is {end-start}")
        return res
    return wrapper
@time_func
def print_name_five_times(name=None):
    '''
    print a name variable five times
    '''
    for i in range(5):
        time.sleep(2)
        print(name)

print(print_name_five_times.__doc__)  # print a name variable five times
print(print_name_five_times.__name__) # print_name_five_times

# more real time examples
import time

# Function-based decorator with parameters
def monitor_performance(unit="seconds"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Start timer
            start_time = time.time()
            result = func(*args, **kwargs)
            # End timer
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            if unit == "milliseconds":
                elapsed_time *= 1000
                print(f"[PERFORMANCE] {func.__name__} executed in {elapsed_time:.2f} ms")
            else:
                print(f"[PERFORMANCE] {func.__name__} executed in {elapsed_time:.2f} s")
                
            return result
        return wrapper
    return decorator

# Applying the decorator with parameters
@monitor_performance(unit="milliseconds")
def user_login(username):
    time.sleep(0.5)  # Simulating API call delay
    print(f"{username} logged in successfully!")

# Call the decorated function
user_login("JohnDoe")




# Class-based decorator with parameters
class RoleBasedAccess:
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles  # Configurable allowed roles

    def __call__(self, func):
        def wrapper(user, *args, **kwargs):
            # Check if the user is authorized
            if user["role"] not in self.allowed_roles:
                print(f"Access Denied: {user['name']} with role '{user['role']}' is not authorized.")
                return None
            print(f"Access Granted: {user['name']} with role '{user['role']}'")
            return func(user, *args, **kwargs)
        return wrapper

# Applying the decorator with dynamic parameters
@RoleBasedAccess(allowed_roles=["admin", "manager"])
def view_reports(user):
    print(f"{user['name']} is viewing sensitive reports!")

# Sample Users
admin_user = {"name": "Alice", "role": "admin"}
guest_user = {"name": "Bob", "role": "guest"}

# Test the decorated function
view_reports(admin_user)  # Access granted
view_reports(guest_user)  # Access denied