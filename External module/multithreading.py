import threading
import time

def worker(num):
    """Thread worker function"""
    print(f'Worker: {num} starting')
    time.sleep(2)
    print(f'Worker: {num} finished')

# Create a thread for each worker
threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
print("All workers have finished execution.")
