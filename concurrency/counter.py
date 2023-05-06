import threading

global i
i = 0
lock = threading.Lock()



# Worker thread for increasing count
class CounterThread(threading.Thread):
    def __init__(self):
        super(CounterThread, self).__init__()
        
    def run(self):
        lock.acquire()
        global i
        i = i + 1
        lock.release()


threads = []
for a in range(0, 10000):
    th = CounterThread()
    th.start()
    threads.append(th)

for thread in threads:
    thread.join()

print(i)