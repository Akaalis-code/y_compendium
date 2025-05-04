import threading
import time

# Define a function for the thread
def print_numbers_A():
    for i in range(100):
        print(f"Number: A:{i}")
        time.sleep(0.1)

def print_numbers_B():
    for i in range(100):
        print(f"Number: B:{i}")
        time.sleep(0.1)

# Create a thread
thread_A = threading.Thread(target=print_numbers_A)
thread_B = threading.Thread(target=print_numbers_B)

# Start the thread
thread_A.start()
thread_B.start()

# Wait for the thread to finish
thread_A.join()
thread_B.join()

print("everything is done")