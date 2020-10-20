"""
Standard Producer/Consumer Threading Pattern
"""

import time
from threading import Thread
from queue import Queue


class Consumer(Thread):
    def __init__(self, _queue, quit_msg):
        Thread.__init__(self)
        self._queue = _queue
        self.quit_msg = quit_msg

    def is_quit_msg(self, msg):
        if isinstance(msg, str) and msg == self.quit_msg:
            return True
        return False

    def run(self):
        while True:
            msg = self._queue.get()
            if self.is_quit_msg(msg):
                break
            print(f"Message: {msg}")
        print("quit requested received shutting down...")


def Producer():
    quit_msg = "quit"
    q = Queue()
    consumer = Consumer(q, quit_msg)
    consumer.start()

    start_time = time.time()

    while time.time() - start_time < 5:
        q.put(f"order received at: {time.time()}")
        time.sleep(1)

    q.put(quit_msg)

    consumer.join()


if __name__ == "__main__":
    Producer()
