import time
import threading

end = None
start = None

def hello():
    global start,end 
    start = time.thread_time()
    x=0
    while x<100000:
        x+=1
    end = time.thread_time()
    
t = threading.Thread(target = hello, args = ())
t.start()
t.join()

print('the time spent is {}'.format(end - start))
    
    
    
import time
import threading 

start = None 
end = None 

def hello(): 
    global start, end 
    start = time.perf_counter()
    x = 0 
    while x < 1000000: 
        x += 1 
    end = time.perf_counter() 

t = threading.Thread(target=hello) 
t.start() 
t.join()

print("Start time:", start, "End time:", end) 
print("Elapsed time: {:.8f} seconds".format(end - start))


import threading
import time

def greet(name, delay): 
    time.sleep(delay) 
    print(f"Hello, {name}! (waited {delay}s)") 

t1 = threading.Thread(target=greet, args=("Yash", 2)) 
t2 = threading.Thread(target=greet, args=("Keshav", 1)) 

t1.start() 
t2.start() 
t1.join() 
t2.join() 
