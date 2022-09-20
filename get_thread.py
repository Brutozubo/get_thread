import logging
import threading
import time
import concurrent.futures

start = time.time()


def get_thread(name):

    time.sleep(1)
    logging.info("Thread %s", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


for i in range(5):
    get_thread(i + 1)

print(time.time() - start)


start = time.time()
def get_thread(name):

    time.sleep(1)
    logging.info("Thread %s", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_thread, range(5))


print(time.time() - start)
