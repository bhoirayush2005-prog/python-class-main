import threading
import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 completed")

def task3():
    print("task3")
    time.sleep(3)
    print("completed")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)
t1.start()
t2.start()
t3.start()



def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")
t1 = threading.Thread(target=task1)
t1.start()
t1.join() # Wait for t3 to complete before continuing