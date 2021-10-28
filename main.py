import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
    def wrapfunc():
      start=time.time()
      func()
      end=time.time()
      print(f"Run Time : {end-start}")
    return wrapfunc

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
    print("For 1st function ",end="")
    
@speed_calc_decorator     
def slow_function():
    for i in range(100000000):
        i * i
    print("For 2nd function ",end="")

fast_function()
slow_function()
