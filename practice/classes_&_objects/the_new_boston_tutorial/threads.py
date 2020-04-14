import threading
import time
import random


class OrMessenger(threading.Thread):
    def run(self):
        for i in range(100):
            print(threading.currentThread().getName())
            time.sleep(random.randrange(1, 4))


x = OrMessenger(name='send out messeges')
y = OrMessenger(name='get messeges')
x.start()
y.start()
