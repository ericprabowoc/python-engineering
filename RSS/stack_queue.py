import time

def timeprint(func):
    def wrapper(*args, **kwargs):
        print("Started")
        start_time = time.time()
        func(*args, **kwargs)
        print("--- %s seconds ---" % (time.time() - start_time))
    
    return wrapper

@timeprint
def stack():
    # Python code to demonstrate Implementing 
    # stack using list
    stack = ["Amar", "Akbar", "Anthony"]
    stack = stack*5
    stack.append("Ram")
    stack.append("Iqbal")
    print(stack)
    
    # Removes the last item
    print(stack.pop())
    
    print(stack)
    
    # Removes the last item
    print(stack.pop())
    
    print(stack)

@timeprint
def queue():
    # Python code to demonstrate Implementing 
    # Queue using list
    queue = ["Amar", "Akbar", "Anthony"]
    queue = queue*5
    queue.append("Ram")
    queue.append("Iqbal")
    print(queue)
    
    # Removes the first item
    print(queue.pop(0))
    
    print(queue)
    
    # Removes the first item
    print(queue.pop(0))
    
    print(queue)

@timeprint
def deque():
    # Python code to demonstrate Implementing 
    # Stack using deque
    from collections import deque
    queue = deque(["Ram", "Tarun", "Asif", "John","Ram", "Tarun", "Asif", "John","Ram", "Tarun", "Asif", "John","Ram", "Tarun", "Asif", "John"])
    print(queue)
    queue.append("Akbar")
    print(queue)
    queue.append("Birbal")
    print(queue)
    print(queue.pop())                 
    print(queue.pop())                 
    print(queue)

@timeprint
def deque_1():
    # Python code to demonstrate Implementing 
    # Queue using deque
    from collections import deque
    queue = deque(["Ram", "Tarun", "Asif", "John","Ram", "Tarun", "Asif", "John","Ram", "Tarun", "Asif", "John","Ram", "Tarun", "Asif", "John"])
    print(queue)
    queue.append("Akbar")
    print(queue)
    queue.append("Birbal")
    print(queue)
    print(queue.popleft())                 
    print(queue.popleft())                 
    print(queue)

stack()
queue()
deque()
deque_1()