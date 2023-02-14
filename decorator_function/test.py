
def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    
    return wrapper

@f1
def f():
    print("Hello")

# f1(f) # not working
# f1(f)() # works
# print(f1(f)) # shows return value from "wrapper" as a function - need to add ()

f()