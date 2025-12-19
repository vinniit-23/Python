"""Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.
"""
def Debugger(func):
    def wrapper(*args,**kwargs):
        args_value =', '.join(str(args) for arg in args)
        kwargs_value = ','.join(f"{k}={v}"for k,v in kwargs.items())
        print(f"calling function name {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args,**kwargs)
    return wrapper
@Debugger
def hello():
    print("hello")
    
@Debugger
def greet(name , greeting="hello"):
    print(f"{greeting},{name}")


greet("vinit", greeting="hii")
