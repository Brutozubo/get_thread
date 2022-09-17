import time
import threading
from threading import Thread

start = time.time()
def get_thread(x):
    time.sleep(1)
    print(f'X = {x}')

for i in range(5):
    get_thread(i + 1)

print(time.time() - start)


start = time.time()
threads = [Thread(target = get_thread, args=(i + 1, )) for i in range (5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
print(time.time() - start)