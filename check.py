# 1. Define the decorator function
def my_logger(original_function):
    def wrapper():
        print(f"LOG: {original_function.__name__} is about to run!")
        original_function() # Run the actual function
        print(f"LOG: {original_function.__name__} finished running.")
    return wrapper

# 2. Apply it using the @ symbol
@my_logger
def say_hello():
    print("Hello, World!")

# 3. Triggering the function
say_hello()


ass= [2,4]*3
print(ass)